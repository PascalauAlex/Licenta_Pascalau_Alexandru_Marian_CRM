import json
import os
import httpx
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from django.conf import settings
from adrf.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import dotenv

from ai_assistant.models import Conversation, Message
from ai_assistant.tools.tools import SYSTEM_PROMPT
from team.models import Team

dotenv.load_dotenv()

OPENAI_URL  = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_URL = getattr(settings, "MCP_SERVER_URL", "http://127.0.0.1:8001/mcp")

_openai_tools_cache = None
_team = None


async def _get_openai_tools():
    """Ask for tools from MCP Server and translate into OpenAI format (cached)"""
    global _openai_tools_cache
    if _openai_tools_cache is None:
        async with Client(StreamableHttpTransport(MCP_URL)) as mcp:
            tools = await mcp.list_tools()
        _openai_tools_cache = [
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description or "",

                    "parameters": t.inputSchema,
                },
            }
            for t in tools
        ]
    return _openai_tools_cache


async def _call_openai(http, messages, tools=None):
    payload = {
        "model": "gpt-4-turbo",
        "messages": messages,
        "temperature": 0.1,
    }
    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = "auto"

    r = await http.post(
        OPENAI_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
        json=payload,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
async def assistant(request):
    user_message = request.data.get('message')
    if not user_message:
        return Response({'error':"No user message"},status=400)

    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        return Response({"error":"Auth header not sent!"})
    team = await Team.objects.aget(members__in=[request.user])

    conversation, created =  await Conversation.objects.aget_or_create(user=request.user, team=team)
    message_user_role = await Message.objects.acreate(conversation=conversation,role='user',content=user_message)




    tools = await _get_openai_tools()

    history = []
    async for m in conversation.messages.order_by("created_at"):
        history.append({"role": m.role, "content": m.content})

    messages = [{"role": "system", "content": SYSTEM_PROMPT}, *history]

    async with httpx.AsyncClient(timeout=60.0) as http:
        first_llm_call = await _call_openai(http,messages,tools=tools)

        if not first_llm_call.get("tool_calls"):
            message_assistant_role = await Message.objects.acreate(conversation=conversation,role='assistant',content=first_llm_call.get('content'))
            return Response({"llm_response":first_llm_call.get("content")},status=200)

        messages.append(first_llm_call)

        transport = StreamableHttpTransport(
            MCP_URL, headers={"Authorization":auth_header}
        )
        async with Client(transport) as mcp:
            for tool_call in first_llm_call["tool_calls"]:
                name = tool_call["function"]["name"]
                try:
                    args = json.loads(tool_call["function"]["arguments"])
                except json.JSONDecodeError:
                    args = {}

                try:
                    result = await mcp.call_tool(name, args, raise_on_error=False)
                except Exception as exc:
                    content = json.dumps({"error": str(exc)})
                else:
                    if result.is_error:
                        text = result.content[0].text if result.content else "tool error"
                        content = json.dumps({"error": text})
                    else:
                        content = json.dumps(result.data, default=str)
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "content": content,
                    }
                )

        final = await _call_openai(http,messages)
        message_assistant_role = await Message.objects.acreate(conversation=conversation,role='assistant',content=final.get('content'))

    return Response({"llm_response": final.get("content")}, status=200)





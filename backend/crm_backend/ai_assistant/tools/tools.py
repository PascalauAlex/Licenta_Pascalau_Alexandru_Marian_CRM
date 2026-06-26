import json

from ai_assistant.tools.lead_tools import get_all_leads, get_leads_by_status, get_leads_by_priority, \
    get_number_of_leads, get_lead_details_by_company, count_leads_by_status
from lead.models import LEAD_STATUSES, LEAD_PRIORITIES

SYSTEM_PROMPT = """You are a CRM assistant for sales team. Your only job is to answer questions about leads, clients, tasks and statistics about them, by calling the provided tools
                #Rules
                1.Always use a tool to get data. Never invert or guess lead/client/task information.
                2.If the user question can be answered with a tool, call it immediately.
                3.If the user asks something outside of the CRM scope (general questions , coding help , weather etc.) respond in one sentance: "I can only help with leads, clients, and tasks."
                5.Never call a tool you don't see in the tools list. Never make up tool names.
                
                
"""


TOOLS = [
    {
        "type":"function",
        "function":{
            "name":"get_all_leads",
            "description":"Get all Leads.",
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_leads_by_status",
            "description":"Get leads by status (eg. new, contacted, inprogress, won, lost ,inactive)",
            "parameters":{
                "type":"object",
                "properties":{
                    "status":{
                        "type":"string",
                        "enum":LEAD_STATUSES,
                        "description":"The status to filter leads by. Must be one of allowed values."
                    }
                },
                "required":["status"],
                "additionalProperties":False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_leads_by_priority",
            "description": "Get leads by priority (eg. low, medium, high)",
            "parameters": {
                "type": "object",
                "properties": {
                    "priority": {
                        "type": "string",
                        "enum": LEAD_PRIORITIES,
                        "description": "The priority to filter leads by. Must be one of allowed values."
                    }
                },
                "required": ["priority"],
                "additionalProperties": False
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_number_of_leads",
            "description":"Get total number of leads ,returns an number"
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_lead_details_by_company",
            "description":"Get lead details by company (e.g Pascalau SRL)",
            "parameters":{
                "type":"object",
                "properties":{
                    "company":{
                        "type":"string",
                        "description":"Company name to filter and retrive lead data."
                    }
                },
                "required":["company"],
                "additionalProperties":False
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"count_leads_by_status",
            "description":"Count the number of leads per status",
        }
    }
]

TOOL_HANDLERS = {
    "get_all_leads":get_all_leads,
    "get_leads_by_status":get_leads_by_status,
    "get_leads_by_priority":get_leads_by_priority,
    "get_number_of_leads":get_number_of_leads,
    "get_lead_details_by_company":get_lead_details_by_company,
    "count_leads_by_status":count_leads_by_status
}

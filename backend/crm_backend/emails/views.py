import base64
from django.conf import settings
from rest_framework.views import APIView
from mailjet_rest import Client
from rest_framework.response import Response
from rest_framework import status, generics

from emails.models import EmailLog
from emails.serializer import EmailSendSerializer, EmailLogSerializer


# Create your views here.


class LeadEmailListView(generics.ListAPIView):
    serializer_class = EmailLogSerializer

    def get_queryset(self):
        lead_id = self.kwargs.get('lead_id') or None
        client_id = self.kwargs.get('client_id') or None

        if lead_id:
            return EmailLog.objects.filter(lead_id=lead_id)
        if client_id:
            return EmailLog.objects.filter(client_id=client_id)
        return EmailLog.objects.none()

class SendEmailView(APIView):
    def post(self, request):
        print("REQUEST DATA:" ,request.data)
        serializer = EmailSendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        clean_data = serializer.validated_data
        to_email = clean_data['to']
        subject = clean_data['subject']
        message = clean_data['message']
        files = request.FILES.getlist('attachments')

        if len(files) > 5:
            return Response({'attachments': ['You cannot add more than 5 files']},status=400)
        for f in files:
            if f.size > 10 * 1024 * 1024:
                return Response({'attachments':[f'File: {f.name} is too big!']},status=400)

        mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')

        # Processing attachaments for Mailjet(Base64)
        processed_attachments = []
        for f in files:
            file_content = f.read()
            encoded_content = base64.b64encode(file_content).decode('utf-8')

            processed_attachments.append({
                "ContentType": f.content_type,
                "Filename": f.name,
                "Base64Content": encoded_content
            })

        # 4. Constructing the object for MailJet
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": settings.MAILJET_FROM_EMAIL,
                        "Name": "Numele Tau/Firma"
                    },
                    "To": [{"Email": to_email}],
                    "Subject": subject,
                    "TextPart": message,
                    "HTMLPart": f"<h3>Mesaj nou</h3><p>{message}</p>",
                    "Attachments": processed_attachments
                }
            ]
        }

        # Sending the mail
        result = mailjet.send.create(data=data)

        if result.status_code == 200:
            EmailLog.objects.create(
                lead_id = request.data.get('lead') or None,
                client_id = request.data.get('client') or None,
                to_email=to_email,
                subject=subject,
                message_body = message,
                sent_by = request.user
            )



            return Response({"message": "Email trimis cu succes!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Eroare la Mailjet", "details": result.json()},
                            status=status.HTTP_400_BAD_REQUEST)



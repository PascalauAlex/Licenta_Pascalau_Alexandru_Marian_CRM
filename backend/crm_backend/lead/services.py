from client.models import Client
from emails.models import EmailLog
from lead.models import LeadNote
from client.models import Note


def convert_lead_to_client(lead):

    lead_note = LeadNote.objects.filter(team=lead.team,lead=lead)
    lead_email_history = EmailLog.objects.filter(lead=lead)

    new_client = Client.objects.create(team=lead.team,name=lead.company,contact_person=lead.contact_person,
                                       email=lead.email, phone=lead.phone, website=lead.website,
                                       created_by=lead.created_by, assigned_to=lead.assigned_to,
                                       last_contacted_date=lead.last_contacted_date,address=lead.address,
                                       source=lead.source)
    if lead_note:
        for item in lead_note:
            client_note = Note.objects.create(team=lead.team,client=new_client,name=item.name,body=item.body,
                                              created_by=item.created_by)
    if lead_email_history:
        for item in lead_email_history:
            EmailLog.objects.create(
                client=new_client, to_email=item.to_email, subject=item.subject,
                message_body=item.message_body, sent_by=item.sent_by,
                mailjet_id=item.mailjet_id, status=item.status,
                opened_at=item.opened_at,
            )



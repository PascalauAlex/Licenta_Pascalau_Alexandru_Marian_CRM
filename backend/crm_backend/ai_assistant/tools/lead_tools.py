from django.db.models.aggregates import Count

from lead.models import Lead
from team.models import Team


async def get_all_leads(team:Team):
    leads = []
    async for lead in Lead.objects.filter(team=team):
        leads.append({
            "company":lead.company,
            "contact_person":lead.contact_person,
            "priority":lead.priority,
            "confidence":lead.confidence
        })
    return leads

async def get_leads_by_status(team: Team,status:str):
    leads:list = []
    async for lead in Lead.objects.filter(team=team,status=status):
        leads.append({
            "company":lead.company,
            "status":lead.status,
            "contact_person":lead.contact_person
        })
    return leads

async def get_leads_by_priority(team : Team,priority:str):
    leads : list = []
    async for lead in Lead.objects.filter(team=team,priority=priority):
        leads.append({
            "company":lead.company,
            "contact_person":lead.contact_person,
            "status":lead.status,
            "priority":lead.priority,
        })

    return leads

async def get_number_of_leads(team:Team):
    count : list = []
    number_of_leads = await Lead.objects.filter(team=team).acount()

    if not number_of_leads:
        return {"error":"Number of leads could not be calculated!"}


    count.append({
        "number_of_leads":number_of_leads
    })
    return count

async def get_lead_details_by_company(team : Team, company: str):
    try:
        lead = await Lead.objects.select_related("assigned_to", "address").aget(
            team=team,
            company=company,
        )
    except Lead.DoesNotExist:
        return {"error": f"Lead '{company}' does not exist."}

    address = None
    if lead.address:
        address = " ".join(filter(None, [
            lead.address.country,
            lead.address.county,
            lead.address.city,
            lead.address.street,
            str(lead.address.street_number) if lead.address.street_number else None,
        ]))


    assigned_to = None
    if lead.assigned_to:
        assigned_to = lead.assigned_to.get_full_name() or lead.assigned_to.username

    return {
        "company": lead.company,
        "contact_person": lead.contact_person,
        "status": lead.status,
        "priority": lead.priority,
        "confidence": lead.confidence,
        "email": lead.email,
        "address": address,
        "assigned_to": assigned_to,
    }

async def count_leads_by_status(team: Team):
    stats : list = []
    return [row async for row in
        Lead.objects.filter(team=team)
            .values("status")
            .annotate(count=Count("id"))
            .order_by("status")
            ]


























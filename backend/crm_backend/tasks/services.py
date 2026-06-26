from django.utils import timezone
from datetime import timedelta
from .models import Tasks, TaskAutomationRule


def trigger_automation_rules(lead, new_status):
    """
    Called after a lead's status changes.
    Finds all active rules for that team + status and creates tasks automatically.
    """
    rules = TaskAutomationRule.objects.filter(
        team=lead.team,
        trigger_status=new_status,
        is_active=True,
    )

    for rule in rules:
        Tasks.objects.create(
            team=lead.team,
            lead=lead,
            title=rule.task_title,
            description=rule.task_description,
            due_date=timezone.now() + timedelta(days=rule.due_days_offset),
            assigned_to=lead.assigned_to if rule.assign_to_owner else None,
        )


        
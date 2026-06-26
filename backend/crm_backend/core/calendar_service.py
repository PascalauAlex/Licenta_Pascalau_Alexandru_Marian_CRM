import requests
from datetime import timedelta
from django.conf import settings
from core.models import GoogleCalendarCredential


def _get_access_token(credential):
    """Recreate access token from stored refresh"""
    if not credential.refresh_token:
        return None
    resp = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'client_id': settings.GOOGLE_OAUTH_CLIENT_ID,
            'client_secret': settings.GOOGLE_OAUTH_CLIENT_SECRET,
            'refresh_token': credential.refresh_token,
            'grant_type': 'refresh_token',
        },
        timeout=10,
    )
    return resp.json().get('access_token') if resp.ok else None


def create_event_for_task(task):
    """Create an event in assigned_to, if the calendar is connected"""
    if task.assigned_to is None:
        print('NO ASSIGNED TO');
        return

    credential = GoogleCalendarCredential.objects.filter(user=task.assigned_to).first()
    if not credential or not credential.refresh_token:
        print('NO CREDENTIAL / REFRESH')
        return

    access_token = _get_access_token(credential)
    if not access_token:
        print('REFRESH FAILED')
        return

    start = task.due_date
    end = start + timedelta(hours=1)

    event = {
        'summary': task.title,
        'description': task.description or '',
        'start': {'dateTime': start.isoformat()},
        'end': {'dateTime': end.isoformat()},
    }

    requests.post(
        'https://www.googleapis.com/calendar/v3/calendars/primary/events',
        headers={'Authorization': f'Bearer {access_token}'},
        json=event,
        timeout=10,
    )
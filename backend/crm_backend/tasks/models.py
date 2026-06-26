from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User
from lead.models import Lead
from team.models import Team
from django.utils import timezone

# Create your models here.




class Tasks(models.Model):
    OPEN = 'open'
    INPROGRESS = 'inprogress'
    CLOSED = 'closed'

    CHOICES_STATUS_TASK = (
        (OPEN, 'open'),
        (INPROGRESS, 'inprogress'),
        (CLOSED, 'closed')
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(choices=CHOICES_STATUS_TASK,default=OPEN)
    due_date = models.DateTimeField()
    lead = models.ForeignKey(Lead,on_delete=models.CASCADE,null=True,blank=True)
    assigned_to = models.ForeignKey(User,on_delete=SET_NULL,null=True,blank=True)
    finished_date = models.DateTimeField(null=True,blank=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='tasks', blank=True, null=True)


    class Meta:
        ordering = ['due_date']
        indexes = [
            models.Index(fields=['team','status'])
        ]

    def __str__(self):
        return f"[{self.title}] {self.status}"





class TaskAutomationRule(models.Model):
    """
    Defines a trigger that automatically creates a Task
    when a Lead reach a specific status

    Exemple : "When a lead is added (STATUS:NEW) -> create task : Contact lead"
    """
    class TriggerStatus(models.TextChoices):
        NEW        = 'new',        'New'
        CONTACTED  = 'contacted',  'Contacted'
        INPROGRESS = 'inprogress', 'In Progress'
        WON        = 'won',        'Won'
        LOST       = 'lost',       'Lost'
        INACTIVE   = 'inactive',   'Inactive'

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='automation_rules',null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)  # ex: "Send invoice on WON"
    trigger_status = models.CharField(max_length=20, choices=TriggerStatus.choices,default=TriggerStatus.NEW)  #
    task_title = models.CharField(max_length=255,null=True,blank=True)  # titlul taskului generat
    task_description = models.TextField(blank=True, null=True)
    due_days_offset = models.PositiveIntegerField(default=1)  # due_date = now + N zile
    assign_to_owner = models.BooleanField(default=True)  # asignează la assigned_to din lead
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} (trigger: {self.trigger_status})"





from django.db import models
from django.contrib.auth.models import User
from lead.models import Lead
from client.models import Client


# Create your models here.


class EmailLog(models.Model):
    lead = models.ForeignKey(Lead,on_delete=models.SET_NULL,null=True, related_name='emails')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True,blank=True)
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    mailjet_id = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20,default='pending')
    opened_at = models.DateTimeField(null=True,blank=True)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"To: {self.to_email} - {self.status}"

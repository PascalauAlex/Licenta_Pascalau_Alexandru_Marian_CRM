from django.db import models
from django.contrib.auth.models import User
from core.models import Address
from team.models import Team


# Create your models here.

NEW = 'new'
ACTIVE = 'active'
INACTIVE = 'inactive'
ON_HOLD = 'on_hold'
FORMER = 'former'
VIP = 'vip'

CHOICES_STATUS = (
(NEW,'New'),
(ACTIVE,'Active'),
(INACTIVE,'Inactive'),
(ON_HOLD,'On Hold'),
(FORMER,'Former'),
(VIP,'VIP')
)





class Client(models.Model):
    team = models.ForeignKey(Team,related_name='clients',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="clients/profile_pictures/%Y/%m/%d/", blank=True, null=True)
    created_by = models.ForeignKey(User,related_name='clients',on_delete=models.CASCADE)
    status = models.CharField(max_length=25,choices=CHOICES_STATUS,default=NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    client_address = models.ForeignKey(Address,on_delete=models.SET_NULL, blank=True, null=True) # WHEN THE ADRESS IS DELETED THE FIELD FILL BE SET ON NULL INSTEAD OF DELETING USER DATA
    assigned_to = models.ForeignKey(User,related_name='assignedClient', blank=True, null=True,on_delete=models.SET_NULL)
    source = models.CharField(max_length=100, blank=True, null=True)
    last_contacted_date = models.DateTimeField(blank=True, null=True)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL, null=True, blank=True, related_name='clients', help_text='Adress of the client')


class Note(models.Model):
    team = models.ForeignKey(Team, related_name='notes', on_delete=models.CASCADE)
    client = models.ForeignKey(Client,related_name='notes',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)





from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.


class Address(models.Model):
    country = CountryField(blank_label='(select country)',default='RO')
    county = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=50)
    building = models.CharField(max_length=50,blank=True,null=True)
    floor = models.CharField(max_length=10, blank=True, null=True)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        parts = [self.county, self.county , self.city, self.street, self.street_number]

        if self.building:
            parts.append(f"B1. {self.building}")
        if self.floor:
            parts.append(f"Floor {self.floor}")

        if self.apartment_number:
            parts.append(f"Ap. {self.apartment_number}")
        if self.zipcode:
            parts.append(f"Zipcode : {self.zipcode}")

        return ", ".join(parts)



class GoogleCalendarCredential(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='google_calendar_credential',null=True,blank=True)
    # access_token = encrypt()
    refresh_token = models.TextField(blank=True,null=True)
    scopes = models.JSONField(blank=True,null=True)
    expiry = models.DateTimeField(null=True,blank=True)
    timestamps = models.DateTimeField(auto_now=True)



from django.db import models
from home.models import UserDetails

# Create your models here.
class Room(models.Model):
    name = models.CharField(primary_key=True, max_length=1000)


class Message(models.Model):
    sno = models.AutoField(primary_key=True)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    room = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000, blank=True)

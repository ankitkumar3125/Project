# Project to populate data through custom management command

Models.py
-----------

from django.db import models


class User(models.Model):
    uid = models.IntegerField()
    Real_Name=models.CharField(max_length=25)
    Time_zone = models.CharField(max_length=100)
    def __str__(self):
        return self.Real_Name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aid = models.IntegerField()
    Start_Time= models.DateTimeField()
    End_Time = models.DateTimeField()


Views.py
-----------

from django.shortcuts import render
from taskapp.serilizer import details
from rest_framework import generics
from taskapp.models import User,ActivityPeriod


class GenericView_List(generics.ListCreateAPIView):
    queryset = User.objects.all()
    queryset = ActivityPeriod.objects.all()
    serializer_class = details

class GenericView_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    queryset = ActivityPeriod.objects.all()
    serializer_class = details

serilizer.py
---------------

from rest_framework import serializers
from .models import User,ActivityPeriod

class details(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
 Pop.py----To populate the data in database through CMC
 ------------------------------------------------------------
 
 from django.core.management.base import BaseCommand, CommandError
from taskapp.models import User, ActivityPeriod

class Command(BaseCommand):
    help = 'Populate data'

    def handle(self, *args, **options):
        User.objects.create()
        User.save()

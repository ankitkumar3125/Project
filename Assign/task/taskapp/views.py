from django.shortcuts import render
from taskapp.serilizer import details
from rest_framework import generics
from taskapp.models import User,ActivityPeriod

# Create your views here.

class GenericView_List(generics.ListCreateAPIView):
    queryset = User.objects.all()
    queryset = ActivityPeriod.objects.all()
    serializer_class = details

class GenericView_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    queryset = ActivityPeriod.objects.all()
    serializer_class = details

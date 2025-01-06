from django.shortcuts import render
from rest_framework import generics
from .models import New
from .serializers import NewSerializer




class NewList(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer

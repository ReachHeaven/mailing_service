from django.shortcuts import render
from rest_framework import generics
from .models import Mailing
from .serializer import MallingSerializer

class MaillingAPIView(generics.ListAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MallingSerializer
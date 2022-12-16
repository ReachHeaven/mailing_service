from rest_framework import serializers
from .models import Mailing, Client, Message


class MallingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "content"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "content"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "content"
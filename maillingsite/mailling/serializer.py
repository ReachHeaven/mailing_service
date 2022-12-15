from rest_framework import serializers
from .models import Mailing


class MallingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "content"

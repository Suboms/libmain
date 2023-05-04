from rest_framework import serializers
from accounts.models import *


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"

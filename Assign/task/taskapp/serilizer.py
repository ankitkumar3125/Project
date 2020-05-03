from rest_framework import serializers
from .models import User,ActivityPeriod

class details(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # class Meta:
    #     model = ActivityPeriod
    #     fields = '__all__'



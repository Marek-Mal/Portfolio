from rest_framework import serializers, viewsets
from django.contrib.auth.models import User

#Serializest For User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

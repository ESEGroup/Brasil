from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        exclude = ('is_staff','user_permissions','password','is_superuser')

class UsarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Usuario
       # depth = 1
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

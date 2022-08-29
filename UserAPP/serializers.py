from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from UserAPP.models import  Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=('UserId', 'UserName', 'Usersurname', 'cedula', 'password', 'address', 'fecha')
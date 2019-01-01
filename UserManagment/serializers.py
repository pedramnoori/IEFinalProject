import hashlib
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from UserManagment.models import User

logger = logging.getLogger('django')


class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'sex', 'birthDate', 'firstName', 'lastName', 'email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
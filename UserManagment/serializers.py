import hashlib
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from UserManagment.models import User

logger = logging.getLogger('django')


class UserLoginSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        userName = data.get('userName')
        password = data.get('password')
        if userName:
            if password:
                try:
                    User.objects.get(password=password, username=userName)
                except Exception as e:
                    logger.log(logging.INFO, e.args)
                    raise ValidationError('username or password wrong')
                return data
            else:
                raise ValidationError('password is empty')
        else:
            raise ValidationError('username is empty')

    class Meta:
        model = User
        fields = ('userName', 'password')

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('userName', 'password', 'sex', 'birthDate', 'firstName', 'lastName', 'email')

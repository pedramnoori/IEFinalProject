import hashlib
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import BaseSerializer

from IE.models import Game

logger = logging.getLogger('django')

class GameSerializer(serializers.ModelSerializer):

    def validate_holdDices(self, data):
        numbers = data.split(',')
        try:
            for number in numbers:
                hold = int(number)
                if hold > 6 or hold < 1:
                    raise ValidationError('error for hold value')
                return data
        except ValueError:
            raise ValidationError("unsupported")

    class Meta:
        model = Game
        fields = ('name','maxScore', 'holdDices', 'maxRoll','diceNumber')

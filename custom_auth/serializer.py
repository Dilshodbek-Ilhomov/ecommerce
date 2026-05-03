from rest_framework import serializers
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be in the format: '+998xxxxxxxxx'."
)

class SMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_validator])

class VerifySMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_validator])
    verification_code = serializers.CharField(min_length=6, max_length=6)
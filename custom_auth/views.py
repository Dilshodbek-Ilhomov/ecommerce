from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import random
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import SMSSerializer, VerifySMSSerializer
from django.conf import settings

User = get_user_model()


class SMSLoginViewSet(viewsets.ViewSet):

    def send_sms(self, request):
        serializer = SMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']

            # Generate a random 6-digit verification code
            verification_code = str(random.randint(100000, 999999))

            # SMS configuration from settings
            sms_url = getattr(settings, 'SMS_URL', 'https://43vvd1.api.infobip.com/sms/2/text/advanced')
            sms_key = getattr(settings, 'SMS_KEY', None)

            if not sms_key:
                return Response({"message": "SMS service is not configured (missing API key)"}, 
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            headers = {
                'Authorization': sms_key,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            payload = {
                'messages': [
                    {
                        'from': 'delx.uz',
                        'destinations': [
                            {
                                'to': phone_number
                            }
                        ],
                        'text': f'Your verification code is {verification_code}'
                    }
                ]
            }

            try:
                response = requests.post(sms_url, json=payload, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    # Store the verification code in cache for 5 minutes
                    cache.set(f"sms_code_{phone_number}", verification_code, 300)
                    return Response({"message": "SMS sent successfully"}, status=status.HTTP_200_OK)
                
                return Response({"message": f"Failed to send SMS: {response.text}"}, 
                                status=status.HTTP_400_BAD_REQUEST)
            except requests.exceptions.RequestException as e:
                return Response({"message": f"SMS service connection error: {str(e)}"}, 
                                status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def verify_sms(self, request):
        serializer = VerifySMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            
            # Use a prefixed key for cache safety
            cached_code = cache.get(f"sms_code_{phone_number}")

            if cached_code and verification_code == cached_code:
                user, created = User.objects.get_or_create(phone_number=phone_number)
                
                # Clear the code after successful verification
                cache.delete(f"sms_code_{phone_number}")

                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'is_new_user': created
                })

            return Response({"message": "Invalid or expired verification code"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
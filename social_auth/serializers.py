from rest_framework import serializers

from .register import register_social_user
from . import google
import os
from rest_framework.exceptions import AuthenticationFailed
from dotenv import load_dotenv

load_dotenv()
class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()
    load_dotenv()
    
    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError('The token is invalid or expired')
        
        if user_data['aud'] != os.getenv('GOOGLE_CLIENT_ID'):
            raise AuthenticationFailed('The token is invalid')
        
        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'
        
        return register_social_user(provider=provider, user_id=user_id, email=email, name=name)
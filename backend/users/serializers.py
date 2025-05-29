from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    """
    Serializer that returns user's information.
    """
    
    preferred_lang = serializers.CharField()
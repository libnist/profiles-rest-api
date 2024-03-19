from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for tesing our APIView"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a model profile object"""
    
    class Meta:
        model = models.UserProfile
        
        fields = ("id", "email", "name", "password")
        
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            }
        }
        
    def create(self, validated_data):
        """Create and return a new user"""
        
        user = models.UserProfile.objects.create_user(**validated_data)
        return user
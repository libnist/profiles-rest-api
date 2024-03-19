from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

from profiles_api import models

from rest_framework import viewsets

from rest_framework import filters

# Create your views here.
class HelloAPIView(APIView):
    """
    Test API View
    """
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional django view",
            "Gives you the must control over your application logic",
            "Is mapped manually to URLs",
        ]
        
        return Response({"message": "Hello", "an_apiview": an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}"
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        return Response({"method": "PATCH"})
    
    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Returns a hello message"""
        
        a_viewset = [
            "Uses Actions (list, create, retrieve, update, partial_update, destroy)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code"
        ]
        
        return Response({"method": request.method, "message": "Hello", "a_viewset": a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}"
            return Response({"method": request.method, "message": message})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_method": request.method})
    
    def update(self, request, pk=None):
        return Response({"http_method": request.method})
    
    def partial_update(self, request, pk=None):
        return Response({"http_method": request.method})
    
    def destroy(self, request, pk=None):
        return Response({"http_method": request.method})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSerializer
    
    queryset = models.UserProfile.objects.all()
    
    authentication_classes = (TokenAuthentication, )
    
    permission_classes = (permissions.UpdateOwnProfile, )
    
    filter_backends = (filters.SearchFilter, )
    
    search_fields = ("name", "email")
    
    
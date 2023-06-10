from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


# Create your views here.
class HelloApiView(APIView):
    """Test ApiView"""
    
    def get(self, request: Request, format= None):
        """Return a list apiview features"""
        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to a traditional django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs ',
        ]
        
        return Response({'message':'hello', 'an_apiview':an_apiview})
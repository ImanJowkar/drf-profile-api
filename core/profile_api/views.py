from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import HelloSerializer

# Create your views here.
class HelloApiView(APIView):
    """Test ApiView"""
    
    serializer_class = HelloSerializer
    
    
    def get(self, request: Request, format= None):
        """Return a list apiview features"""
        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to a traditional django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs ',
        ]
        
        return Response({'message':'hello', 'an_apiview':an_apiview})
    
    
    def post(self, request: Request):
        """Create a hello message with our name"""
        my_ser = self.serializer_class(data=request.data)
        if my_ser.is_valid():
            name = my_ser.validated_data.get('name')
            msg = f"Hello {name}"
            return Response({"message":msg})
        
        else:
            return Response(my_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request: Request, pk=None):
        """Handle updating an objects"""
        return Response({"method": "PUT"}) 
    
    
    
    def patch(self, request: Request, pk=None):
        """Handle a partial updating an objects"""
        return Response({"method": "PATCH"})
    
     
    def delete(self, request: Request, pk=None):
        """Handle delete an objects"""
        return Response({"method": "delete"}) 
           
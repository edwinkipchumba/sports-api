from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import sports
from . serializers import sportsSerializer

# handling GET and POST request
class sport(APIView):                  # inherits from an APIView
 
    def get(self, request):
        obj = sports.objects.all()      # Getting all values
        serializer = sportsSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        data = request.data             # Data passed in body
        serializer = sportsSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # if error
    
    # handling PUT and DELETE requests
class sportbyid(APIView):    # Handle entry-specific operations
 
    def get_object(self, id):
        try:
            return sports.objects.get(id=id)
        except sports.DoesNotExist as e:
            return Response({"error": "Not found."},status=404)
        
    def get(self, request, id=None):
        instance = self.get_object(id)   
        serializer = sportsSerializer(instance) 
        return Response(serializer.data)
    
    def put(self, request, id=None):
        data = request.data            # Data passed to overwrite
        instance = self.get_object(id)   
        serializer = sportsSerializer(instance, data=data)   
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        instance = self.get_object(id)
        serializer = sportsSerializer(instance)
        instance.delete()
        return Response(serializer.data)
    
# Edit the views.py file and add this
class LandingPage(APIView):
    def get(self, request):
        s = {'message' : 'Welcome', 'documentation' : '<specify notes>'}
        return Response(s)
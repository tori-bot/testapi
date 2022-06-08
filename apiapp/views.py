from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#handle all the status code responses.
from .models import  MoringaMerch
from .serializer import MerchSerializer
# Create your views here.
class MerchList(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_merch = MoringaMerch.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = MerchSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
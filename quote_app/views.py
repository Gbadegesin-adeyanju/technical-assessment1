from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quote
from .serializers import QuoteSerializers 
from rest_framework.views import APIView
# Create your views here.

class quoteview(APIView):
    
    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializers(quotes, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = QuoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        



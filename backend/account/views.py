from django.shortcuts import render
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response


class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            return Response({'msg':'Regi Success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

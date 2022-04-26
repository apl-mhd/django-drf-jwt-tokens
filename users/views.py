import email
from typing_extensions import Self
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from users.models import User
from .serializers import UserSerializer
from users import serializers 
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed





def test(request):

    return HttpResponse('hello')

class RegisterView(APIView):
    def post(Self, request):
        serializer =  UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User Not Found")
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        return Response({
            'message': 'success'
        })


from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.
from IEProject.settings import onlineUsers
from UserManagment.models import User
from UserManagment.permissions import Authenticate
from UserManagment.serializers import UserSignupSerializer, UserLoginSerializer


class Log_in (APIView):
    authentication_classes = ()
    def get(self, request):
        return render(request, 'pages/login.html')

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=User.objects.get(username=username))
            res = HttpResponseRedirect(redirect_to='/home')
            res.set_cookie('tok',token.key, 1212123,123124,'/')
            return res
        else:
            return Response({'message': 'login failed!'}, status=status.HTTP_401_UNAUTHORIZED)



class SignUp(APIView):

    authentication_classes = ()

    def get(self, request):
        return render(request, 'pages/signup.html')

    def post(self, request):
        serial = UserSignupSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return HttpResponseRedirect(redirect_to='')

class Test(APIView):
    permission_classes = (Authenticate,)

    def get(self, request):
        return Response("mammad")

class Home(APIView):

    def get(self, request):
        return render(request, 'pages/index.html', {'onlineuser': onlineUsers, 'summary': request.user})


class Logout(APIView):

    def get(self, request):
        try:
            Token.objects.get(user=request.user).delete()
            onlineUsers.remove(request.user)
            return render(request, 'pages/logout.html')
        except:
            return Response('Error')


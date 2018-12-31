from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler

from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework.views import APIView

# Create your views here.
from UserManagment.serializers import UserSignupSerializer


class Log_in (APIView):
    def get(self, request):
        return render(request, 'pages/login.html')

    def post(self, request):
        serial = UserSignupSerializer(request.data)
        serial.is_valid(raise_exception=True)



class SignUp(APIView):

    def get(self, request):
        return render(request, 'pages/signup.html')

    def post(self, request):
        serial = UserSignupSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return HttpResponseRedirect(redirect_to='')


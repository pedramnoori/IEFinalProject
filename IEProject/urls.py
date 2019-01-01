"""IEProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from IE.views import gameDesign, GameView, newgame
from UserManagment.views import Log_in, Test, Home, Logout
from UserManagment.views import SignUp

onlineUsers = set()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', Log_in.as_view()),
    path('up', SignUp.as_view()),
    path('test',Test.as_view()),
    path('home',Home.as_view()),
    path('logout',Logout.as_view(),name='logout'),
    path('gameDesign',gameDesign.as_view(),name='gamedesign'),
    path('gameView',GameView.as_view(),name='gameview'),
    path('newgame',newgame.as_view(),name='newgame'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

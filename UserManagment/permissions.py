from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from IEProject.settings import onlineUsers
from UserManagment.models import User


class Authenticate(BasePermission):
    def has_permission(self, request, view):
        cookie = request.COOKIES.get('tok')
        try:
            Token.objects.get(key=cookie)
            return True
        except:
            return False


    def has_object_permission(self, request, view, obj):
        pass


class AuthenticateUser(BaseAuthentication):
    def authenticate(self, request):
        cookie = request.COOKIES.get('tok')
        if not cookie:
            return None

        try:
            user_id = Token.objects.get(key=cookie).user_id
            user = User.objects.get(id=user_id)
        except Exception:
            raise None
        onlineUsers.add(user)
        return user, user.isAdmin
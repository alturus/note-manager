from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.users.permissions import IsAdminOrCreateOnly
from api.users.serializers import UserSerializer


class UserTokenObtainPairView(TokenObtainPairView):
    throttle_scope = 'user-login'


class UserTokenRefreshView(TokenRefreshView):
    throttle_scope = 'user-login'


class UserList(generics.ListCreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (
        IsAdminOrCreateOnly,
    )
    throttle_scope = None

    def get_throttles(self):
        if self.request.method in ['POST', ]:
            self.throttle_scope = 'user-registration'
        return super().get_throttles()

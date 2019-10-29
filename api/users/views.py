from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        tokens = serializer.instance.token_pair
        data = serializer.data
        data.update({
            "access": str(tokens['access']),
            "refresh": str(tokens['refresh']),
        })
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

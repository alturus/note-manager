from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    @property
    def token_pair(self):
        """Get a new token pair"""
        refresh_token = RefreshToken.for_user(self)
        refresh_token['is_admin'] = self.is_admin
        access_token = refresh_token.access_token
        token_pair = {
            'refresh': refresh_token,
            'access': access_token,
        }
        return token_pair

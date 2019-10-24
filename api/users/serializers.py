from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_admin',
            'password',
        )
        write_only_fields = ('password',)

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    @property
    def data(self):
        tokens = self.instance.token_pair
        content = {
            "username": str(self.instance.username),
            "access": str(tokens['access']),
            "refresh": str(tokens['refresh']),
        }
        return content

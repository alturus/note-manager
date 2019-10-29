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
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

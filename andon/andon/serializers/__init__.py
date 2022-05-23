from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenObtainSerializer,
    TokenRefreshSerializer
)
from andon.andon.libs.code import success_dict


class MyTokenObtainSerializer(TokenObtainSerializer):
    default_error_messages = {"no_active_account": "username or password not true"}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer, MyTokenObtainSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['username'] = self.user.username
        data["name"] = self.user.name

        return success_dict("success", data)
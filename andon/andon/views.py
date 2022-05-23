from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import (
    MyTokenObtainPairSerializer,
    MyTokenRefreshSerializer
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairView
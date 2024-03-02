from rest_framework import viewsets

from users.models import User
from users.serializers import UserSignUpSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
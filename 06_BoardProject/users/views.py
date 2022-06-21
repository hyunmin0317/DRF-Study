from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from users.serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
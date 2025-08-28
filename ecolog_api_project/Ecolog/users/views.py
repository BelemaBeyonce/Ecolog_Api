from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserRegistrationSerializer, UserSerializer
from .models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
# Create your views here.

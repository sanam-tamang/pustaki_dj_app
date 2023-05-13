from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserRegistrationSerializer, UserDetailSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from tokengen.models import get_tokens_for_user
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserDetail(APIView):
     permission_classes = (IsAuthenticated,)
     def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

class RegisterUserView(APIView):
     def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
           user = serializer.save()
           token = get_tokens_for_user(user)
           return Response({'user': serializer.data,
                             'token': token},
                          status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes= [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        serializer = UserDetailSerializer(request.data)
        user = authenticate(email=email, password=password)
        if user:
            login(request,user)
            return Response({
                'user': serializer.data,
                'token':  get_tokens_for_user(user)} , status= status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
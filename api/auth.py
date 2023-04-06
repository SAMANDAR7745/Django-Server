from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer, PasswordSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .permissions import IsAdminOrIsSelf


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response({"key": token.key})


class LogOutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out"})


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})


# GET -> get -> list() -> retrieve()

class UserViewSet(viewsets.ModelViewSet):  # ViewSet
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serailizer = RegisterSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrIsSelf])
    def set_password(self, request, pk):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({"status": "Password Set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def recend_users(self, request):
        return Response({"detail", 'working'})

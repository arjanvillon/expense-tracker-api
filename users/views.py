from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .serializers import (
    LoginSerializer, RegisterSerializer, UserSerializer, )


class RegisterApiView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1],

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token,
        })


class LoginApiView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token,
            }
        )


class UserApiView(generics.RetrieveAPIView):

    serializers = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return self.request.user

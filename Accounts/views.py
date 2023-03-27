from django.contrib.auth import authenticate, login, logout
from rest_framework import authentication, permissions, status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from Accounts.models import UserProfile
from Accounts.serializers import UpdateSerializer, UserSerializer
from Accounts.tokens import create_jwt_pair_for_user


class AccountView(CreateAPIView):
    serializer_class = UserSerializer


class UpdateView(UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateSerializer

    def get_object(self):
        return get_object_or_404(UserProfile, id=self.request.user.id)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Login Successfull", "tokens": tokens["refresh"]}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


    # def post(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         login(request, user)
    #         return Response()
    #     else:
    #         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteAccountView(APIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = UserProfile.objects.filter(pk=self.kwargs['pk'])
        user.delete()
        return Response({"result": "user delete"})

    def get_queryset(self):
        return UserProfile.objects.all()


# class ShowView(ListAPIView):
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         return UserProfile.objects.all()


class LogOutView(APIView):

    def post(self, request):
        if self.request.user.is_authenticated:
            try:
                logout(request)
            except Exception:
                return Response("Logout Failed")
        return Response("Successfully logout")


class getAccountView(RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(UserProfile, id=self.kwargs['id'])

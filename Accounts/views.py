from django.contrib.auth import authenticate, login, logout
from rest_framework import authentication, permissions, status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from Accounts.models import UserProfile
from Accounts.serializers import UpdateSerializer, UserSerializer


class AccountView(CreateAPIView):
    serializer_class = UserSerializer


class UpdateView(UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateSerializer

    def get_object(self):
        return get_object_or_404(UserProfile, id=self.kwargs['id'])


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response("Success")
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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

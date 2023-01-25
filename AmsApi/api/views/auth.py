from django.contrib.auth import login, logout
from rest_framework import permissions, status, views
from rest_framework.response import Response

from .. import serializers


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class Logout(views.APIView):
    
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
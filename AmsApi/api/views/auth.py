from django.contrib.auth import login, logout
from rest_framework import permissions, status, views
from rest_framework.response import Response
from django.middleware.csrf import get_token

from .. import serializers


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)
        response = Response(None, status=status.HTTP_202_ACCEPTED)
        response["XSRF-TOKEN"] = get_token(request)
        response["Access-Control-Expose-Headers"] = "XSRF-TOKEN"

        print(response["XSRF-TOKEN"])
        return response


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

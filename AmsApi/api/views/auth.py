from django.contrib.auth import login, logout
from rest_framework import permissions, status, views
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import HttpResponse, JsonResponse

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
        response = HttpResponse(status=status.HTTP_202_ACCEPTED)
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        response["Access-Control-Allow-Credentials"] = "true"
        
    # Set the X-CSRFToken header
        response["X-CSRFToken"] = get_token(request)
        return response

    def get(self, request):
        current_user = request.user
        print(current_user)
        if current_user.is_authenticated:
            user = serializers.UserSerializer(instance=current_user).data
            response = JsonResponse(data=user)
        else:
            response = JsonResponse(
                {"status_code": 403, "error": "Unathorized"},
                status=403,
            )
        return response


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

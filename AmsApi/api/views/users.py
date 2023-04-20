from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import permissions, status, views
from rest_framework.response import Response

from . import serializers


class UsersView(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, _request, id=None):
        try:
            if id is not None:
                user_instance = User.objects.get(id=id)
                data = serializers.UserSerializer(instance=user_instance).data
                response = JsonResponse(data=data)
            else:
                users_instance = User.objects.all()
                data = serializers.UserSerializer(
                    instance=users_instance, many=True
                ).data
                response = JsonResponse(data=data, safe=False)
        except User.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"}, status=404
            )

        return response

    def post(self, request):
        print(request.data)
        serializer = serializers.UserSerializer(
            data=self.request.data, context={"request": self.request}
        )
        if serializer.is_valid():
            print("inside")
            instance = serializer.save()
            print(instance)
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

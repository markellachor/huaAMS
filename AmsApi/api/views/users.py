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
                print(id)
                user_instance = User.objects.get(id=id)
                data = serializers.UserSerializer(instance=user_instance).data
                response = JsonResponse(data=data)
            else:
                users_instance = User.objects.all()
                data = serializers.UserSerializer(
                    instance=users_instance, many=True).data
                response = JsonResponse(data=data, safe=False)
        except User.DoesNotExist:
            response = JsonResponse({
                'status_code': 404,
                'error': 'The resource was not found'
            }, status=404)

        return response

    def post(self, request):
        body = request.data
        # TODO: Validate data -> Middlewares?
        user = User.objects.create_user(
            username=body['username'],
            email=body['email'],
            last_name=body['lastName'],
            first_name=body['firstName'])

        print(user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

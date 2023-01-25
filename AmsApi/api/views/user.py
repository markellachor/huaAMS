from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, permissions, views

from . import serializers


class MeView(generics.RetrieveAPIView):
    """
    Class representing "me" where me is a logged-in user
    """
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user

class UserView(views.APIView):
    permission_classes = ([permissions.IsAdminUser])

    def get(self, _request, id):
        try:
            user_instance = User.objects.get(id=id)
            data = serializers.UserSerializer(instance=user_instance).data
            response = JsonResponse(data=data)
        except User.DoesNotExist:
            response = JsonResponse({
                'status_code': 404,
                'error': 'The resource was not found'
            }, status=404)

        return response

class UsersView(views.APIView):
    permission_classes = ([permissions.IsAdminUser])
    def get(self, _request):
        users_instance = User.objects.all()
        data = serializers.UserSerializer(instance=users_instance, many=True).data
        print(data)
        response = JsonResponse(data=data, safe=False)

        return response
        
        
import json
from rest_framework import permissions, status, views, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse

from api.models import Asset
from django.views.decorators.csrf import csrf_exempt

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
    permission_classes = (permissions.IsAdminUser,)

    def get(self, _request):
        users_instance = User.objects.all()
        data = serializers.UserSerializer(
            instance=users_instance, many=True).data
        print(data)
        response = JsonResponse(data=data, safe=False)

        return response

    def post(self, request):
        body = request.data
        # body = json.loads(body_unicode)
        content = body['username']
        print(body) 
        user = User.objects.create_user(
            username=body['username'], email=body['email'], last_name=body['lastName'], first_name=body['firstName'])
        # user.set_password(body['password'])
        # user.save()
        print(user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AssetView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, _request):
        asset_instance = Asset.objects.all()
        data = serializers.AssetSerializer(
            instance=asset_instance, many=True).data
        print(data)
        response = JsonResponse(data=data, safe=False)

        return response

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # content = body['username']
        print(body)
        # user = User.objects.create_user(username=body['username'], email=body['email'],last_name=body['lastName'],first_name=body['firstName'])
        # user.set_password(body['password'])
        # user.save()
        # print(user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
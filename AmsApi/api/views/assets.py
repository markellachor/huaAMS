import json

from api.models import Asset
from django.http import JsonResponse
from rest_framework import permissions, status, views
from rest_framework.response import Response

from .. import serializers


class AssetView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, _request):
        asset_instance = Asset.objects.all()
        data = serializers.AssetSerializer(instance=asset_instance, many=True).data
        print(data)
        response = JsonResponse(data=data, safe=False)

        return response

    def post(self, request):
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        # content = body['username']
        print(body)

        # user.set_password(body['password'])
        # user.save()
        # print(user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

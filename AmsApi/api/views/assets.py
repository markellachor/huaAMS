from api.models import Asset
from django.http import JsonResponse
from rest_framework import permissions, status, views
from rest_framework.response import Response

from .. import serializers


class AssetView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = serializers.AssetSerializer(
            data=request.data, context={"request": self.request}
        )

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, _request, id=None):
        try:
            if id is not None:
                asset_instance = Asset.objects.get(id=id)
                data = serializers.AssetSerializer(instance=asset_instance).data
                response = JsonResponse(data=data)
            else:
                assets_instance = Asset.objects.all()
                data = serializers.AssetSerializer(
                    instance=assets_instance, many=True
                ).data
                response = JsonResponse(data=data, safe=False)
        except Asset.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"}, status=404
            )

        return response

    def delete(self, _request, id):
        try:
            asset_instance = Asset.objects.get(id=id)
            asset_instance.delete()
            response = Response(None, status=status.HTTP_200_OK)
        except Asset.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"},
                status=404,
            )

        return response

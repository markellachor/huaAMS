from api.models import Asset
from api.views.base_view import BaseView
from rest_framework import permissions, status
import qrcode
from django.http import HttpRequest, JsonResponse
# from rest_framework import permissions, serializers, , views
from rest_framework.response import Response

from .. import serializers


class AssetView(BaseView):
    serializer = serializers.AssetSerializer
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAuthenticated,)
    model = Asset

    def post(self, request: HttpRequest):
        serializer = serializers.AssetSerializer(
            data=request.data, context={"request": self.request}
        )

        if serializer.is_valid():
            serializer.save()
            asset_id = serializer.data.get("id")

            qr_path = "api/static/assets/asset_qr_" + str(asset_id) + ".png"
            img = qrcode.make(asset_id)
            img.save(qr_path)

            asset = Asset.objects.filter(id=asset_id).update(
                qr_path="static/assets/asset_qr_" + str(asset_id) + ".png"
            )

            return JsonResponse(data={"id":asset_id}, safe=False)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
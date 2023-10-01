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

    def get(self, request, id=None):
        current_user = request.user
        if id is not None:
            try:
                model_instance = self.model.objects.filter(id=id).filter(user_id=current_user.id)
                data = self.serializer(instance=model_instance).data
                response = JsonResponse(data=data)
            except self.model.DoesNotExist:
                response = JsonResponse(
                    {"status_code": 404, "error": "The resource was not found"},
                    status=404,
                )
        else:
            if current_user.is_superuser:
                model_instance = self.model.objects.all()
            else:
                model_instance = self.model.objects.filter(user_id=current_user.id)
            data = self.serializer(instance=model_instance, many=True).data
            response = JsonResponse(data=data, safe=False)

        return response
from api.models import Asset
from api.views.base_view import BaseView
from rest_framework import permissions

from .. import serializers


class AssetView(BaseView):
    serializer = serializers.AssetSerializer
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAuthenticated,)
    model = Asset

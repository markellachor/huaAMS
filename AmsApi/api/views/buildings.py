from api.models import Building
from api.views.base_view import BaseView
from rest_framework import permissions

from . import serializers


class BuildingsView(BaseView):
    serializer = serializers.BuildingSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Building

from api.models import Department
from rest_framework import permissions

from AmsApi.api.views.base_view import BaseView

from . import serializers


class DepartmentsView(BaseView):
    serializer = serializers.DepartmentSerializer
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAuthenticated,)
    model = Department

from api.models import Department
from api.views.base_view import BaseView
from rest_framework import permissions

from . import serializers


class DepartmentsView(BaseView):
    serializer = serializers.DepartmentSerializer
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAuthenticated,)
    model = Department

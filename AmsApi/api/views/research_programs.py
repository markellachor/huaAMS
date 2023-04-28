from api.models import ResearchProgram
from api.views.base_view import BaseView
from rest_framework import permissions

from . import serializers


class ResearchProgramsView(BaseView):
    serializer = serializers.ResearchProgramSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = ResearchProgram

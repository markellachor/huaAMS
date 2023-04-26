from api.models import Asset
from api.serializers.building import BuildingSerializer
from api.serializers.department import DepartmentSerializer
from api.serializers.research_program import ResearchProgramSerializer
from api.serializers.user import UserSerializer
from rest_framework import serializers


class AssetSerializer(serializers.ModelSerializer):
    building = BuildingSerializer()
    department = DepartmentSerializer()
    research_program = ResearchProgramSerializer()
    user_id = UserSerializer()

    class Meta:
        model = Asset
        depth = 1
        fields = "__all__"

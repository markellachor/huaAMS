from api.models import Asset, Building, Department, ResearchProgram
from api.serializers.user import UserModel
from rest_framework import serializers


class AssetSerializer(serializers.ModelSerializer):
    building = serializers.SlugRelatedField(queryset=Building.objects.all(), slug_field='id')
    department = serializers.SlugRelatedField(queryset=Department.objects.all(), slug_field='id')
    research_program = serializers.SlugRelatedField(queryset=ResearchProgram.objects.all(), slug_field='id')
    user_id = serializers.SlugRelatedField(queryset=UserModel.objects.all(), slug_field='id')

    class Meta:
        model = Asset
        depth = 1
        fields = "__all__"

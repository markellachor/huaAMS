from api.models import ResearchProgram
from rest_framework import serializers


class ResearchProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchProgram
        fields = ["title", "researcher", "description"]

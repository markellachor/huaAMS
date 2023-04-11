from api.models import Asset
from rest_framework import serializers


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'description',
            'category',
            'pieces'
        ]

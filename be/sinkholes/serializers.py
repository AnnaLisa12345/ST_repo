from rest_framework import serializers
from .models import Sinkhole


class SinkholeSerializer(serializers.ModelSerializer):
    """Serializer for Sinkhole model."""
    
    class Meta:
        model = Sinkhole
        fields = [
            'id', 'name', 'description', 'latitude', 'longitude',
            'diameter', 'depth', 'risk_level', 'geological_type',
            'soil_type', 'bedrock_type', 'water_table_depth',
            'discovery_date', 'last_inspection', 'is_active',
            'created_at', 'updated_at'
        ]

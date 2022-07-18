from rest_framework.serializers import ModelSerializer
from .models import RadarSensor


class TestDataSerializer(ModelSerializer):
    class Meta:
        model = RadarSensor
        fields = '__all__'

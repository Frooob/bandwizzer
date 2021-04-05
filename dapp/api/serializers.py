from rest_framework import serializers

from .models import Measurement


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ("id", "connection", "speed_download", "speed_upload", "date")

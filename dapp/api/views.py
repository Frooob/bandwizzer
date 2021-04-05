from django.shortcuts import render

from rest_framework import viewsets

from .serializers import MeasurementSerializer
from .models import Measurement


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all().order_by('date')
    serializer_class = MeasurementSerializer

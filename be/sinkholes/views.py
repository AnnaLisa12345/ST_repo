from django.shortcuts import render
from rest_framework import viewsets
from .models import Sinkhole
from .serializers import SinkholeSerializer


class SinkholeViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing sinkhole data."""
    queryset = Sinkhole.objects.all()
    serializer_class = SinkholeSerializer

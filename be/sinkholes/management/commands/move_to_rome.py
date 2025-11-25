from django.core.management.base import BaseCommand
from sinkholes.models import Sinkhole
import random


class Command(BaseCommand):
    help = 'Update all sinkhole coordinates to Rome area'

    def handle(self, *args, **kwargs):
        # Rome center coordinates
        rome_lat = 41.9028
        rome_lon = 12.4964
        
        # Get all sinkholes
        sinkholes = Sinkhole.objects.all()
        
        # Update each sinkhole with coordinates around Rome
        for i, sinkhole in enumerate(sinkholes):
            # Spread them around Rome (within ~0.5 degrees, roughly 50km radius)
            lat_offset = random.uniform(-0.5, 0.5)
            lon_offset = random.uniform(-0.5, 0.5)
            
            sinkhole.latitude = rome_lat + lat_offset
            sinkhole.longitude = rome_lon + lon_offset
            sinkhole.save()
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {sinkholes.count()} sinkholes to Rome area')
        )

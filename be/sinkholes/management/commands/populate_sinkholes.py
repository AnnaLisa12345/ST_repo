from django.core.management.base import BaseCommand
from sinkholes.models import Sinkhole
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate database with sample sinkhole data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Sinkhole.objects.all().delete()
        
        # Sample data for sinkholes around the world
        sample_sinkholes = [
            {
                'name': 'Dead Sea Sinkholes',
                'description': 'Cluster of sinkholes forming along the Dead Sea shore due to water level decline.',
                'latitude': 31.5590,
                'longitude': 35.4732,
                'diameter': 15.0,
                'depth': 12.0,
                'risk_level': 'HIGH',
                'geological_type': 'DISSOLUTION',
                'soil_type': 'Salt deposits',
                'bedrock_type': 'Limestone',
                'water_table_depth': 5.0,
                'is_active': True,
            },
            {
                'name': 'Guatemala City Sinkhole',
                'description': 'Massive urban sinkhole that appeared in Guatemala City.',
                'latitude': 14.6341,
                'longitude': -90.5069,
                'diameter': 20.0,
                'depth': 30.0,
                'risk_level': 'CRITICAL',
                'geological_type': 'COLLAPSE',
                'soil_type': 'Volcanic pumice',
                'bedrock_type': 'Volcanic rock',
                'water_table_depth': 15.0,
                'is_active': False,
            },
            {
                'name': 'Xiaozhai Tiankeng',
                'description': 'One of the world\'s deepest sinkholes in Chongqing, China.',
                'latitude': 28.8333,
                'longitude': 109.4833,
                'diameter': 537.0,
                'depth': 662.0,
                'risk_level': 'LOW',
                'geological_type': 'KARST',
                'soil_type': 'Karst soil',
                'bedrock_type': 'Limestone',
                'water_table_depth': 100.0,
                'is_active': False,
            },
            {
                'name': 'Bayou Corne Sinkhole',
                'description': 'Sinkhole formed from salt dome cavern collapse in Louisiana.',
                'latitude': 29.9528,
                'longitude': -91.1806,
                'diameter': 350.0,
                'depth': 240.0,
                'risk_level': 'HIGH',
                'geological_type': 'ANTHROPOGENIC',
                'soil_type': 'Swamp deposits',
                'bedrock_type': 'Salt dome',
                'water_table_depth': 2.0,
                'is_active': True,
            },
            {
                'name': 'Berezniki Sinkhole',
                'description': 'Mining-related sinkhole in Berezniki, Russia.',
                'latitude': 59.4089,
                'longitude': 56.8200,
                'diameter': 80.0,
                'depth': 78.0,
                'risk_level': 'CRITICAL',
                'geological_type': 'ANTHROPOGENIC',
                'soil_type': 'Clay and sand',
                'bedrock_type': 'Potash deposits',
                'water_table_depth': 10.0,
                'is_active': True,
            },
            {
                'name': 'Winter Park Sinkhole',
                'description': 'Famous sinkhole in Winter Park, Florida.',
                'latitude': 28.5997,
                'longitude': -81.3392,
                'diameter': 107.0,
                'depth': 27.0,
                'risk_level': 'MEDIUM',
                'geological_type': 'SUBSIDENCE',
                'soil_type': 'Sandy soil',
                'bedrock_type': 'Limestone',
                'water_table_depth': 8.0,
                'is_active': False,
            },
            {
                'name': 'Bimmah Sinkhole',
                'description': 'Beautiful water-filled sinkhole in Oman.',
                'latitude': 23.0367,
                'longitude': 59.0894,
                'diameter': 40.0,
                'depth': 20.0,
                'risk_level': 'LOW',
                'geological_type': 'KARST',
                'soil_type': 'Coastal deposits',
                'bedrock_type': 'Limestone',
                'water_table_depth': 0.5,
                'is_active': False,
            },
            {
                'name': 'Daisetta Sinkhole',
                'description': 'Large sinkhole in Daisetta, Texas.',
                'latitude': 30.1116,
                'longitude': -94.6441,
                'diameter': 182.0,
                'depth': 45.0,
                'risk_level': 'MEDIUM',
                'geological_type': 'SUBSIDENCE',
                'soil_type': 'Clay and sand',
                'bedrock_type': 'Salt dome',
                'water_table_depth': 12.0,
                'is_active': False,
            },
            {
                'name': 'Qattara Depression',
                'description': 'Massive natural depression in Egypt.',
                'latitude': 29.5333,
                'longitude': 27.1333,
                'diameter': 80000.0,
                'depth': 133.0,
                'risk_level': 'LOW',
                'geological_type': 'DISSOLUTION',
                'soil_type': 'Sand and salt',
                'bedrock_type': 'Limestone',
                'water_table_depth': 50.0,
                'is_active': False,
            },
            {
                'name': 'Corvette Museum Sinkhole',
                'description': 'Sinkhole that swallowed classic cars in Kentucky.',
                'latitude': 36.9872,
                'longitude': -86.4497,
                'diameter': 12.0,
                'depth': 18.0,
                'risk_level': 'MEDIUM',
                'geological_type': 'KARST',
                'soil_type': 'Clay',
                'bedrock_type': 'Limestone',
                'water_table_depth': 20.0,
                'is_active': False,
            },
            {
                'name': 'Devil\'s Sinkhole',
                'description': 'Deep karst sinkhole in Texas.',
                'latitude': 30.0500,
                'longitude': -100.3667,
                'diameter': 12.0,
                'depth': 107.0,
                'risk_level': 'LOW',
                'geological_type': 'KARST',
                'soil_type': 'Rocky soil',
                'bedrock_type': 'Limestone',
                'water_table_depth': 80.0,
                'is_active': False,
            },
            {
                'name': 'Macungie Sinkhole',
                'description': 'Urban sinkhole in Pennsylvania.',
                'latitude': 40.5156,
                'longitude': -75.5538,
                'diameter': 9.0,
                'depth': 15.0,
                'risk_level': 'HIGH',
                'geological_type': 'SUBSIDENCE',
                'soil_type': 'Urban fill',
                'bedrock_type': 'Limestone',
                'water_table_depth': 7.0,
                'is_active': True,
            },
            {
                'name': 'Blue Hole (Dahab)',
                'description': 'Famous diving spot, underwater sinkhole in Egypt.',
                'latitude': 28.5833,
                'longitude': 34.5167,
                'diameter': 52.0,
                'depth': 130.0,
                'risk_level': 'LOW',
                'geological_type': 'KARST',
                'soil_type': 'Coral reef',
                'bedrock_type': 'Limestone',
                'water_table_depth': 0.0,
                'is_active': False,
            },
            {
                'name': 'Zacatón Sinkhole',
                'description': 'Deepest water-filled sinkhole in the world, Mexico.',
                'latitude': 23.8333,
                'longitude': -99.1667,
                'diameter': 116.0,
                'depth': 339.0,
                'risk_level': 'LOW',
                'geological_type': 'KARST',
                'soil_type': 'Volcanic deposits',
                'bedrock_type': 'Limestone',
                'water_table_depth': 0.0,
                'is_active': False,
            },
            {
                'name': 'Sarisarinama Sinkholes',
                'description': 'Tepui sinkholes in Venezuela.',
                'latitude': 4.6667,
                'longitude': -64.3167,
                'diameter': 352.0,
                'depth': 314.0,
                'risk_level': 'LOW',
                'geological_type': 'COLLAPSE',
                'soil_type': 'Organic soil',
                'bedrock_type': 'Sandstone',
                'water_table_depth': 50.0,
                'is_active': False,
            },
        ]
        
        # Create sinkhole objects with random dates
        created_count = 0
        for data in sample_sinkholes:
            # Add random dates
            discovery_days_ago = random.randint(100, 3650)
            inspection_days_ago = random.randint(10, 365)
            
            data['discovery_date'] = date.today() - timedelta(days=discovery_days_ago)
            data['last_inspection'] = date.today() - timedelta(days=inspection_days_ago)
            
            Sinkhole.objects.create(**data)
            created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sinkholes')
        )

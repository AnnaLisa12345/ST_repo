from django.core.management.base import BaseCommand
from sinkholes.models import Sinkhole
from datetime import date, timedelta
import random
import csv
import os


class Command(BaseCommand):
    help = 'Populate database with real sinkhole data from CSV'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Sinkhole.objects.all().delete()
        
        # Read CSV file with real sinkhole locations
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            '..',
            'detected_cavity_clusters.csv'
        )
        
        sinkholes_created = 0
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for idx, row in enumerate(reader, start=1):
                    longitude = float(row['Longitude'])
                    latitude = float(row['Latitude'])
                    
                    # Create sinkhole with basic data
                    Sinkhole.objects.create(
                        name=f'Sinkhole #{idx}',
                        description=f'Detected cavity cluster at coordinates ({latitude:.6f}, {longitude:.6f})',
                        latitude=latitude,
                        longitude=longitude,
                        diameter=random.uniform(5.0, 25.0),  # Random diameter between 5-25m
                        depth=random.uniform(3.0, 15.0),  # Random depth between 3-15m
                        risk_level=random.choice(['low', 'medium', 'high']),
                        geological_type=random.choice(['KARST', 'DISSOLUTION', 'SUBSIDENCE', 'COLLAPSE']),
                        soil_type='Urban soil',
                        bedrock_type='Limestone',
                        water_table_depth=random.uniform(5.0, 20.0),
                        is_active=True,
                    )
                    sinkholes_created += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {sinkholes_created} sinkholes from CSV data')
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'CSV file not found at {csv_path}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error reading CSV: {str(e)}')
            )

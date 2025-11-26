import os
import sys
import django

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sinkholes_project.settings')
django.setup()

from sinkholes.models import Sinkhole
from sinkholes.serializers import SinkholeSerializer
import json

# Get all sinkholes
sinkholes = Sinkhole.objects.all()
data = SinkholeSerializer(sinkholes, many=True).data

# Write to JSON file
output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fe', 'sinkholes-data.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(list(data), f, indent=2)

print(f"Exported {len(data)} sinkholes to {output_file}")

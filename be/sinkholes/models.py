from django.db import models


class Sinkhole(models.Model):
    """Model representing a sinkhole with geological and risk data."""
    
    RISK_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    diameter = models.FloatField(help_text="Diameter in meters", null=True, blank=True)
    depth = models.FloatField(help_text="Depth in meters", null=True, blank=True)
    risk_level = models.CharField(max_length=20, choices=RISK_LEVELS, default='low')
    geological_type = models.CharField(max_length=100, blank=True)
    soil_type = models.CharField(max_length=100, blank=True)
    bedrock_type = models.CharField(max_length=100, blank=True)
    water_table_depth = models.FloatField(help_text="Water table depth in meters", null=True, blank=True)
    discovery_date = models.DateField(null=True, blank=True)
    last_inspection = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

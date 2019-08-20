from django.db import models
from datetime import datetime

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30);
    description = models.TextField(max_length=100);
    opening_time = models.TimeField(default=datetime.now);
    closing_time = models.TimeField(default=datetime.now);
    
    def __str__(self):
        return self.name

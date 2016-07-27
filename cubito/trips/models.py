from __future__ import unicode_literals

from django.db import models

# Create your models here.
class trips(models.Model):
	id = models.AutoField(primary_key=True)
	trip_id = models.CharField(max_length=255)
	trip_data = models.TextField()
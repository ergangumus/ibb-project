from django.contrib.gis.db import models

class CarPark(models.Model):
    park_name = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    park_type_id = models.CharField(max_length=255)
    park_type_desc = models.CharField(max_length=255)
    capacity_of_park = models.PositiveIntegerField()
    working_time = models.CharField(max_length=50)
    county_name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.park_name
from django.db import models

class Farms(models.Model):
    location = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    sensor_type = models.CharField(max_length=50)
    values = models.IntegerField()


    def __str__(self):
        return self.location

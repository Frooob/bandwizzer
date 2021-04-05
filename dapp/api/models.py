from django.db import models


class Measurement(models.Model):
    connection = models.CharField(max_length=60)
    speed_download = models.IntegerField()
    speed_upload = models.IntegerField()
    date = models.DateTimeField()

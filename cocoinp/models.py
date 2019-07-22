from django.db import models


# Create your models here.
class Buyer(models.Model):
    hotel_name = models.TextField()
    hotel_address = models.TextField()
    mobile_number = models.IntegerField()
    qty_required = models.IntegerField()
    date_required = models.DateField()

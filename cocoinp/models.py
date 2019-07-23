from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.TextField()
    address = models.TextField()
    mobile_number = models.IntegerField()
    qty_required = models.IntegerField()
    date_required = models.DateField()

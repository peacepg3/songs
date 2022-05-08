from django.db import models
from datetime import datetime
from idpass.models import pgattribute
# Create your models here.
class todomodel(models.Model):

    work = models.TextField()
    time = models.IntegerField()
    date = models.DateField(default=datetime.today())
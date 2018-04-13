from django.db import models
from django_mysql.models import ListCharField

#Create your models here.
class Bus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    start_busstop = models.CharField(max_length=100)
    end_busstop = models.CharField(max_length=100)
    stops = ListCharField(base_field=models.CharField(max_length=100), size=1000, max_length=1000*101)


class Busstop(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    bus_visit = ListCharField(base_field=models.CharField(max_length=100), size=1000, max_length=1000*101)


class Graph(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    adj_list = ListCharField(base_field=models.CharField(max_length=100), size=1000, max_length=1000*101)


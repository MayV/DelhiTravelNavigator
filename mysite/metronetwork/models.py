from django.db import models
from django_mysql.models import ListCharField, ListTextField

# Create your models here.
class Metro(models.Model):
    color = models.CharField(max_length=100, primary_key=True)
    start_metrostation = models.CharField(max_length=100)
    end_metrostation = models.CharField(max_length=100)
    stations = ListCharField(base_field=models.CharField(max_length=100), size=1000, max_length=1000*101)
    distance = ListTextField(base_field=models.IntegerField(), size=1000)


class Graph(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    adj_List = ListCharField(base_field=models.CharField(max_length=100), size=1000, max_length=1000*101)
    dist_List = ListTextField(base_field=models.IntegerField(), size=100)

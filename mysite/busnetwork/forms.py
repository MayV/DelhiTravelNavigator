from django import forms
from .models import Bus,Busstop,Graph
from django.shortcuts import render

class BusRouteForm(forms.Form):
    uinpsrc = forms.CharField(label="Source Bus Stop ", max_length=100)
    uinpdest = forms.CharField(label="Destination Bus Stop ", max_length=100)

    def clean_message(self,uinpsrc,unipdtest):
        flag_d=0
        flag_s=0
        bus_set = Bus.objects.all()
        for obj in bus_set:
            for stop in obj.stops:
                if stop == uinpsrc:
                    flag_s = 1
                if stop == uinpdest:
                    flag_d = 1

        if flag_d == 0 or flag_s == 0:
            return -1
        else:
            return 1



class BusForm(forms.Form):
    uinpbus = forms.CharField(label="Enter Bus Number ", max_length=100)

    def clean_message(self,uinpbus):
        bus_set = Bus.objects.all()
        for obj in bus_set:
            if obj.id == uinpbus:
                return 1
        return -1

class BusStopForm(forms.Form):
    uinpbusstop = forms.CharField(label="Enter Bus Stop ", max_length=100)

    def clean_message(self,uinpbusstop):
        busstop_set = Busstop.objects.all()
        for obj in busstop_set:
            if obj.name == uinpbusstop:
                return 1
        return -1

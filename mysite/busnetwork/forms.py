from django import forms
from .models import Bus,Busstop,Graph
from django.shortcuts import render

class BusRouteForm(forms.Form):
    uinpsrc = forms.CharField(label="Source Bus Stop ", max_length=100)
    uinpdest = forms.CharField(label="Destination Bus Stop ", max_length=100)

    uinpsrc.widget.attrs.update({'list':'busstop'})
    uinpdest.widget.attrs.update({'list':'busstop'})

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

    '''def get_all(self):
        busstop_set = Busstop.objects.all()
        busstop = set()
        for obj in busstop_set:
            busstop.add(obj.name)
		return busstop'''

    def get_all(self):
        busstop_set=Busstop.objects.all()
        busstop=set()
        for obj in busstop_set:
            busstop.add(obj.name)
        return busstop

class BusForm(forms.Form):
    uinpbus = forms.CharField(label="Enter Bus Number ", max_length=100)

    uinpbus.widget.attrs.update({'list':'bus'})

    def clean_message(self,uinpbus):
        bus_set = Bus.objects.all()
        for obj in bus_set:
            if obj.id == uinpbus:
                return 1
        return -1

    '''def get_all(self):
		bus_no_set=Bus.objects.all()
		bus_no = set()
		for obj in bus_no_set:
			bus_no.add(obj.id)
		return bus_no'''

    def get_all(self):
        bus_no_set=Bus.objects.all()
        bus_no =set()
        for obj in bus_no_set:
            bus_no.add(obj.id)
        return bus_no

class BusStopForm(forms.Form):
    uinpbusstop = forms.CharField(label="Enter Bus Stop ", max_length=100)

    uinpbusstop.widget.attrs.update({'list':'busstop'})

    def clean_message(self,uinpbusstop):
        busstop_set = Busstop.objects.all()
        for obj in busstop_set:
            if obj.name == uinpbusstop:
                return 1
        return -1

    def get_all(self):
        busstop_set=Busstop.objects.all()
        busstop=set()
        for obj in busstop_set:
            busstop.add(obj.name)
        return busstop

from django import forms
from .models import Bus, Busstop


class BusRouteForm(forms.Form):
    uinpsrc = forms.CharField(label="Source Bus Stop ", max_length=100)
    uinpdest = forms.CharField(label="Destination Bus Stop ", max_length=100)

    uinpsrc.widget.attrs.update({'list':'busstop'}) #Add list attribute and mentions datalist_id in it.
    uinpdest.widget.attrs.update({'list':'busstop'})

    def clean_message(self,uinpsrc,uinpdest):
        flagsrc=0
        flagdest=0
        busList = Bus.objects.all()
        for b in busList:
            for stop in b.stops:
                if stop == uinpsrc:
                    flagsrc = 1
                if stop == uinpdest:
                    flagdest = 1
        if flagsrc == 0 or flagdest == 0:
            return -1
        else:
            return 1

    def get_all(self):
        busstopList = Busstop.objects.all()
        busstops=set()
        for stop in busstopList:
            busstops.add(stop.name)
        return busstops


class BusForm(forms.Form):
    uinpbus = forms.CharField(label="Enter Bus Number ", max_length=100)

    uinpbus.widget.attrs.update({'list':'bus'})

    def clean_message(self,uinpbus):
        busList = Bus.objects.all()
        for b in busList:
            if b.id == uinpbus:
                return 1
        return -1

    def get_all(self):
        busList = Bus.objects.all()
        buses=set()
        for obj in busList:
            buses.add(obj.id)
        return buses


class BusStopForm(forms.Form):
    uinpbusstop = forms.CharField(label="Enter Bus Stop ", max_length=100)

    uinpbusstop.widget.attrs.update({'list':'busstop'})

    def clean_message(self,uinpbusstop):
        busstopList = Busstop.objects.all()
        for obj in busstopList:
            if obj.name == uinpbusstop:
                return 1
        return -1

    def get_all(self):
        busstopList = Busstop.objects.all()
        busstops=set()
        for obj in busstopList:
            busstops.add(obj.name)
        return busstops

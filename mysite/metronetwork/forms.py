from django import forms
from .models import Metro, Graph


class MetroRouteForm(forms.Form):
    uinpsrc = forms.CharField(label="Source Metro Station ", max_length=100)
    uinpdest = forms.CharField(label="Destination Metro Station ", max_length=100)

    uinpsrc.widget.attrs.update({'list': 'station'})
    uinpdest.widget.attrs.update({'list': 'station'})

    def clean_message(self, unipsrc, unipdest):
        flagsrc = 0
        flagdest = 0
        metroList = Metro.objects.all()
        for m in metroList:
            for station in m.stations:
                if station == unipdest:
                    flagdest = 1
                if station == unipsrc:
                    flagsrc = 1
        if flagsrc == 0 or flagdest == 0:
            return -1
        else:
            return 1

    def get_all(self):
        stationList = Graph.objects.all()
        stations = set()
        for obj in stationList:
            stations.add(obj.name)
        return stations


class MetroForm(forms.Form):
    uinpmetro = forms.CharField(label="Enter Metro Line Colour ", max_length=100)

    uinpmetro.widget.attrs.update({'list': 'color'})

    def clean_message(self, unipmetro):
        flag = 0
        metroList = Metro.objects.all()
        for m in metroList:
            if m.color == unipmetro:
                flag = 1
                break
        if flag == 0:
            return -1
        else:
            return 1

    def get_all(self):
        metroList = Metro.objects.all()
        colors = set()
        for obj in metroList:
            colors.add(obj.color)
        return colors

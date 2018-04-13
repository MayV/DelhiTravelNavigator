from django import forms

class BusRouteForm(forms.Form):
    uinpsrc = forms.CharField(label="Source Bus Stop ", max_length=100)
    uinpdest = forms.CharField(label="Destination Bus Stop ", max_length=100)

class BusForm(forms.Form):
    uinpbus = forms.CharField(label="Enter Bus Number ", max_length=100)

class BusStopForm(forms.Form):
    uinpbusstop = forms.CharField(label="Enter Bus Stop ", max_length=100)

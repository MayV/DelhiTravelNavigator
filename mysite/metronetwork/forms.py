from django import forms

class MetroRouteForm(forms.Form):
    uinpsrc = forms.CharField(label="Source Metro Station ", max_length=100)
    uinpdest = forms.CharField(label="Destination Metro Station ", max_length=100)

class MetroForm(forms.Form):
    uinpmetro = forms.CharField(label="Enter Metro Line Colour ", max_length=100)

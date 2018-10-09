from django import forms
from .models import Metro,Graph
from django.shortcuts import render

class MetroRouteForm(forms.Form):
	uinpsrc = forms.CharField(label="Source Metro Station ", max_length=100)
	uinpdest = forms.CharField(label="Destination Metro Station ", max_length=100)

	uinpsrc.widget.attrs.update({'list':'station', 'class':'text-box'})
	uinpdest.widget.attrs.update({'list':'station','class':'text-box'})

	def clean_message(self, unipsrc, unipdest):

		#uinpdest = self.cleaned_data.get("uinpdest").upper()
		#unipsrc = self.cleaned_data.get("uinpsrc").upper()
		flag1 = 0
		flag2 = 0
		metro_set = Metro.objects.all()
		for obj in metro_set:
			for station in obj.stations:
				if station == unipdest:
					flag2 = 1
				if station == unipsrc:
					flag1 = 1

		if flag1 == 0 or flag2 == 0:
			return -1
		else:
			return 1

	def get_all(self):
		station_set = Graph.objects.all()
		station = set()
		for obj in station_set:
			station.add(obj.name)
		return station


class MetroForm(forms.Form):
	uinpmetro = forms.CharField(label="Enter Metro Line Colour ", max_length=100)

	uinpmetro.widget.attrs.update({'list': 'colour', 'class':'text-box'})

	def clean_message(self, unipmetro) :
		flag = 0
		metro_set = Metro.objects.all()
		for obj in metro_set:
			if obj.color == unipmetro:
				flag = 1
				break

		if flag == 0:
			return -1
		else:
			return 1

	def get_all(self):
		metro_set = Metro.objects.all()
		color_set = set()
		for obj in metro_set:
			color_set.add(obj.color)
		return color_set

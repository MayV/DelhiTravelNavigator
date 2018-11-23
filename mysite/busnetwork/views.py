from django.shortcuts import render
from .forms import BusRouteForm, BusForm, BusStopForm
from .bus_route_algorithm import main_route
from .bus_details_algorithm import main_bus
from .busstop_details_algorithm import main_busstop
from .modelsUtil.fillbusstop import main1
from .modelsUtil.buildgraph import main2


def get_busroutequery(request):
    if request.method=='POST':  #if post meathod process form data.
        form = BusRouteForm(request.POST)
        if form.is_valid():
            uinpsrc = form.cleaned_data.get("uinpsrc").upper()
            uinpdest = form.cleaned_data.get("uinpdest").upper()
            if form.clean_message(uinpsrc, uinpdest) != -1:
                retval = main_route(uinpsrc, uinpdest)
                blank_form = BusRouteForm()
                busstops = blank_form.get_all()
                context = {'srcstop': uinpsrc, 'deststop': uinpdest, 'allRoutes': retval, 'form': blank_form, 'busstops': busstops}
                return render(request, 'busnetwork/display_busroute.html', context)
            else:
                context = {}
                return render(request, 'busnetwork/wrong_input.html', context)
        else:   #Never executed.
            context = {}
            return render(request, 'busnetwork/wrong_input.html', context)
    else:   #if get method, create a blank form.
        blank_form = BusRouteForm()
        busstops = blank_form.get_all()
        context = {'form': blank_form, 'busstops':busstops}
        return render(request, 'busnetwork/busroute_query.html', context)


def get_busquery(request):
    if request.method=='POST':  #if post meathod process form data.
        form = BusForm(request.POST)
        if form.is_valid():
            uinpbus = form.cleaned_data.get("uinpbus").upper()
            if form.clean_message(uinpbus) != -1:
                retval = main_bus(uinpbus)
                blank_form = BusForm()
                buses = blank_form.get_all()
                context = {'busDetails': retval, 'form': blank_form, 'buses': buses}
                return render(request, 'busnetwork/display_bus.html', context)
            else:
                context = {}
                return render(request, 'busnetwork/wrong_input.html', context)
        else:   #Never executed.
            context = {}
            return render(request, 'busnetwork/wrong_input.html', context)
    else:   #if get method, create a blank form.
        blank_form = BusForm()
        buses = blank_form.get_all()
        context = {'form': blank_form, 'buses':buses}
        return render(request, 'busnetwork/bus_query.html', context)


def get_busstopquery(request):
    if request.method=='POST':  #if post meathod process form data.
        form = BusStopForm(request.POST)
        if form.is_valid():
            uinpbusstop = form.cleaned_data.get("uinpbusstop").upper()
            if form.clean_message(uinpbusstop) != -1:
                retval = main_busstop(uinpbusstop)
                blank_form = BusStopForm()
                busstops = blank_form.get_all()
                context = {'busstopDetails': retval, 'form': blank_form, 'busstops': busstops}
                return render(request, 'busnetwork/display_busstop.html', context)
            else:
                context = {}
                return render(request, 'busnetwork/wrong_input.html', context)
        else:   #Never executed.
            context = {}
            return render(request, 'busnetwork/wrong_input.html', context)
    else:   #if get method, create a blank form.
        blank_form = BusStopForm()
        busstops = blank_form.get_all()
        context = {'form': blank_form, 'busstops':busstops}
        return render(request, 'busnetwork/busstop_query.html', context)


def initialize_bus_database(request):    #To fill database automatically.
    main1()
    main2()
    context = {}
    return render(request, 'busnetwork/init_complete.html', context)

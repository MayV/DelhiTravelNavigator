from django.shortcuts import render
from .forms import MetroRouteForm, MetroForm
from .metro_route_algorithm import main_route
from .metro_details_algorithm import main_metro
from .modelsUtil.buildgraph import main1
from .calculate_metrofare import sunday_token, sunday_card, otherday_token, otherday_peakcard,otherday_nonpeakcard


def get_metroroutequery(request):
    if request.method=='POST':  #if post meathod process form data.
        form = MetroRouteForm(request.POST)
        if form.is_valid():
            uinpsrc = form.cleaned_data.get("uinpsrc").upper()
            uinpdest = form.cleaned_data.get("uinpdest").upper()
            retval = main_route(uinpsrc, uinpdest)
            distance = retval[-1][0]
            retval = retval[0:len(retval)-1]
            travelcost = {}
            travelcost['sun_card'] = sunday_card(float(distance))
            travelcost['sun_token'] = sunday_token(float(distance))
            travelcost['other_peakcard'] = otherday_peakcard(float(distance))
            travelcost['other_nonpeakcard'] = otherday_nonpeakcard(float(distance))
            travelcost['other_token'] = otherday_token(float(distance))
            blank_form = MetroRouteForm()
            context = {'srcstation': uinpsrc, 'deststation': uinpdest, 'allRoutes': retval, 'cost': travelcost, 'form': blank_form}
            return render(request, 'metronetwork/display_metroroute.html', context)
        else:
            context = {}
            return render(request, 'metronetwork/wrong_input.html', context)
    else:   #if get method, create a blank form.
        blank_form = MetroRouteForm()
        context = {'form': blank_form}
        return render(request, 'metronetwork/metroroute_query.html', context)


def get_metroquery(request):
    if request.method=='POST':  #if post meathod process form data.
        form = MetroForm(request.POST)
        if form.is_valid():
            uinpmetro = form.cleaned_data.get("uinpmetro").upper()
            retval = main_metro(uinpmetro)
            blank_form = MetroForm()
            context = {'metroDetails': retval, 'form': blank_form}
            return render(request, 'metronetwork/display_metro.html', context)
        else:
            context = {}
            return render(request, 'metronetwork/wrong_input.html', context)
    else:   #if get method, create a blank form.
        blank_form = MetroForm()
        context = {'form': blank_form}
        return render(request, 'metronetwork/metro_query.html', context)


def initialize_metro_database(request):    #To fill database automatically.
    main1()
    context = {}
    return render(request, 'metronetwork/init_complete.html', context)

from .models import Busstop

def main_busstop(uinpbusstop):
    busstopobjectList = Busstop.objects.all()
    for i in range(len(busstopobjectList)):
        if uinpbusstop == busstopobjectList[i].name:
            retval = {}
            retval['busstop_name'] = busstopobjectList[i].name
            retval['all_buses'] = busstopobjectList[i].bus_visit
            return retval
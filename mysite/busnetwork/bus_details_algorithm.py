from .models import Bus

def main_bus(uinpbus):
    busobjectList = Bus.objects.all()
    for i in range(len(busobjectList)):
        if uinpbus == busobjectList[i].id:
            retval = {}
            retval['bus_id'] = busobjectList[i].id
            retval['start_busstop'] = busobjectList[i].start_busstop
            retval['end_busstop'] = busobjectList[i].end_busstop
            retval['all_busstops'] = busobjectList[i].stops
            return retval
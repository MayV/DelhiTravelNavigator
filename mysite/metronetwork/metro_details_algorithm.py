from .models import Metro

def main_metro(uinpmetro):
    metroobjectList = Metro.objects.all()
    retval = {}
    retval['metro_color'] = uinpmetro
    if uinpmetro == 'BLUE':
        for i in range(len(metroobjectList)):
            if metroobjectList[i].color == 'BLUE':
                retval['start_station'] = metroobjectList[i].start_metrostation
                retval['end_station'] = ''
                retval['all_stations'] = metroobjectList[i].stations
        for i in range(len(metroobjectList)):
            if metroobjectList[i].color == 'BLUE 2':
                retval['end_station'] = metroobjectList[i].end_metrostation
                retval['sub_stations1'] = metroobjectList[i].stations
        for i in range(len(metroobjectList)):
            if metroobjectList[i].color == 'BLUE 3':
                retval['end_station'] = metroobjectList[i].end_metrostation + ', ' + retval['end_station']
                retval['sub_stations2'] = metroobjectList[i].stations
        return retval
    elif uinpmetro == 'GREEN':
        for i in range(len(metroobjectList)):
            if metroobjectList[i].color == 'GREEN':
                retval['start_station'] = metroobjectList[i].start_metrostation
                retval['end_station'] = ''
                retval['all_stations'] = metroobjectList[i].stations
        for i in range(len(metroobjectList)):
            if metroobjectList[i].color == 'GREEN 2':
                retval['end_station'] = metroobjectList[i].end_metrostation
                retval['sub_stations1'] = metroobjectList[i].stations
        for i in range(len(metroobjectList)):
            if metroobjectList[i].color == 'GREEN 3':
                retval['end_station'] = metroobjectList[i].end_metrostation + ', ' + retval['end_station']
                retval['sub_stations2'] = metroobjectList[i].stations
        return retval
    else:
        for i in range(len(metroobjectList)):
            if uinpmetro == metroobjectList[i].color:
                retval['start_station'] = metroobjectList[i].start_metrostation
                retval['end_station'] = metroobjectList[i].end_metrostation
                retval['all_stations'] = metroobjectList[i].stations
        return retval

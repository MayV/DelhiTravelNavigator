import json
from busnetwork.models import Bus

file = json.load(open('moovit_data.json'))

for k in file: 
    obj = Bus()
    obj.id = k
    temp1 = file[k][0]
    obj.start_busstop = temp1.upper()
    temp2 = file[k][-1]
    obj.end_busstop = temp2.upper()
    for i in range(len(file[k])):
        temp = file[k][i]
        if ',' in temp:
            temp.replace(',', '-')
        obj.stops.append(temp.upper())
    obj.save()

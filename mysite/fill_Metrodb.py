import json
from metronetwork.models import Metro
file1 = json.load(open('metro_data.json'))
file2 = json.load(open('metro_dist.json'))
for k in file1:
    obj = Metro()
    obj.color = k.upper()
    obj.start_metrostation = file1[k][0].upper()
    obj.end_metrostation = file1[k][-1].upper()
    for j in range(len(file1[k])):
        obj.stations.append(file1[k][j].upper())
    for j in range(1,len(file2[k])):
        obj.distance.append(int(float(file2[k][j])*10) - int(float(file2[k][j-1])*10))
    obj.save()

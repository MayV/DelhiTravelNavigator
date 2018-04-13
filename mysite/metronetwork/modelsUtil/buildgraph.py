from metronetwork.models import Metro, Graph

def main1():
    metroobjList = Metro.objects.all()
    visitedstations = {}
    for i in range(len(metroobjList)):
        stationList = metroobjList[i].stations
        for j in range(len(stationList)):
            if stationList[j] not in visitedstations:
                visitedstations[stationList[j]] = True
                obj = Graph()
                obj.name = stationList[j]
                obj.save()
    grphobjList = Graph.objects.all()
    for i in range(len(metroobjList)):
        stationList = metroobjList[i].stations
        distanceList = metroobjList[i].distance
        for j in range(1,len(stationList)):
            u = stationList[j-1]
            v = stationList[j]
            d = distanceList[j-1]
            for k in range(len(grphobjList)):
                if u == grphobjList[k].name:
                    if v not in grphobjList[k].adj_List:
                        grphobjList[k].adj_List.append(v)
                        grphobjList[k].dist_List.append(d)
                        grphobjList[k].save()
                        break
            for k in range(len(grphobjList)):
                if v == grphobjList[k].name:
                    if u not in grphobjList[k].adj_List:
                        grphobjList[k].adj_List.append(u)
                        grphobjList[k].dist_List.append(d)
                        grphobjList[j].save()
                        break

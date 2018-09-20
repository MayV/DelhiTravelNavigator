from .models import Graph
from .models import Metro
def getallRoutes(src, grph, stationvisited, dest):
    if src.name == dest.name:
        baseretval = [[dest.name]]
        return baseretval
    allPaths = []
    for i in range(len(src.adj_List)):
        if src.adj_List[i] not in stationvisited:
            #if src.adj_List[i] in dp:
             #   retpath = dp[src.adj_list[i]]
            stationvisited[src.adj_List[i]] = True
            retpath = getallRoutes(grph[src.adj_List[i]], grph, stationvisited, dest)
                #dp[src.adj_List[i]] = retpath
            stationvisited.pop(src.adj_List[i])
            for j in range(len(retpath)):
                #tempdist = int(retpath[j][0])+(src.dist_List[i])
                allPaths.append([src.name]+retpath[j])
    return allPaths


def main_route(uinpsrc, uinpdest):
    grphobjList = Graph.objects.all()   #List of Graph objects
    metroobjList = Metro.objects.all()
    grph = {}   #Dictionary of Graph objects.
    for i in range(len(grphobjList)):
        grph[grphobjList[i].name] = grphobjList[i]
    src = grph[uinpsrc]     #Object of Graph type.
    dest = grph[uinpdest]   #Object of Graph type.
    stationvisited = {}    #Marks the stations which are visited.
    stationvisited[src.name]=True
    retval = getallRoutes(src, grph, stationvisited, dest)
    minroutelen = 1000

    airport = {}
    for i in range(len(metroobjList)):
        if metroobjList[i].color == "AIRPORT EXPRESS":
            for station in metroobjList[i].stations:
                if station != "New Delhi" and station != "Dwarka Sec-21":
                    airport[station] = True


    temp = []
    for i in range(len(retval)):
        temp.append(retval[i])
    k = 0
    if src.name not in airport and dest.name not in airport:
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if temp[i][j] in airport:
                    retval.pop(k)
                    k = k-1
                    break
            k = k+1

    airport["NEW Delhi"] = True
    airport["DWARKA SEC-21"] = True

    for i in range(len(retval)):
        if minroutelen > len(retval[i]):
            minroutelen = len(retval[i])
    bestroutes = []
    for i in range(len(retval)):
        if len(retval[i]) <= minroutelen + 5:
            bestroutes.append(retval[i])
    mindist = 10000
    mindistrouteindx = -1
    for i in range(len(bestroutes)):
        dist = 0
        for j in range(len(bestroutes[i])-1):
            if bestroutes[i][j] in airport and bestroutes[i][j+1] in airport:
                continue
            u = grph[bestroutes[i][j]]
            v = bestroutes[i][j+1]
            for k in range(len(u.adj_List)):
                if u.adj_List[k] == v:
                    dist = dist + u.dist_List[k]
                    break
        if dist < mindist:
            mindist = dist
            mindistrouteindx = i

    station2=""
    if src.name in airport and dest.name in airport:
        station1 = src.name
        station2 = dest.name
    elif src.name in airport or dest.name in airport:
        station1 = src.name
        for name in bestroutes[mindistrouteindx]:
            if name != station1 and (name == "NEW DELHI" or name == "DWARKA SEC-21"):
                station2 = name
                break
    temp = 0
    if station2 != "":
        temp = 10

    bestroutes.append([mindistrouteindx])
    actualdist = str(float(mindist/10.0))
    bestroutes.append([actualdist])
    bestroutes.append([temp])
    return bestroutes
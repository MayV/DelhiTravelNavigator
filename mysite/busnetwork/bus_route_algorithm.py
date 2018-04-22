from collections import deque
from .models import Graph, Bus, Busstop

def Utilfunc(shrtpath, si, stps):
    chkpointindx = si
    for i in range(si+1,len(shrtpath)):
        if shrtpath[i] in stps:
            chkpointindx = i
    return chkpointindx

def basefunc(src, dest, shrtpath, si, buses, busstop, busvisited, dp):
    busList = busstop[src].bus_visit
    allPaths = []
    for i in range(len(busList)):
        b = busList[i]
        if b not in busvisited:
            stps = buses[b].stops
            chkpointindx = Utilfunc(shrtpath, si, stps)
            chkpoint = shrtpath[chkpointindx]
            if chkpoint == src:
                continue
            elif chkpoint == dest:
                basepath = [b, dest]
                allPaths.append(basepath)
            else:
                if chkpoint in dp:
                    retpath = dp[chkpoint]
                else:
                    busvisited[b] = True
                    retpath = basefunc(chkpoint, dest, shrtpath, chkpointindx, buses, busstop, busvisited, dp)
                    dp[chkpoint] = retpath
                    busvisited.pop(b)
                for j in range(len(retpath)):
                    allPaths.append([b,chkpoint]+retpath[j])
    return allPaths

def main_route(uinpsrc, uinpdest):
    # uinpsrc and uinpdest are strings.
    grphobjList = Graph.objects.all()
    grph = {}   # Dictionary of busstop name as key and object as value.
    for i in range(len(grphobjList)):
        grph[grphobjList[i].name] = grphobjList[i]
    src = grph[uinpsrc]
    # bfs requirements.
    queue = deque([src])  # Queue of objects.
    parent = {uinpsrc: "****"}  # Both key and value are string.
    visited = {uinpsrc: True}  # Key is string whereas value is boolean.
    flag = False
    while queue:
        if flag:
            break
        temp = queue.popleft()
        for adjNode in temp.adj_list:
            if adjNode not in visited:
                queue.append(grph[adjNode])
                parent[adjNode] = temp.name
                visited[adjNode] = True
                if adjNode == uinpdest:
                    flag = True
                    break
    shrtpath = [uinpdest]
    p = parent[uinpdest]
    while p != "****":
        shrtpath = [p] + shrtpath
        p = parent[p]
    busobjList = Bus.objects.all()
    busstopobjList = Busstop.objects.all()
    buses = {}  # Dictionary of bus id as key and object as value.
    busstops = {}   # Dictionary of busstops as key and object as value.
    for i in range(len(busobjList)):
        buses[busobjList[i].id] = busobjList[i]
    for i in range(len(busstopobjList)):
        busstops[busstopobjList[i].name] = busstopobjList[i]
    busvisited = {}   # To mark which bus has been boarded so that it is not boarded again.
    dp = {}     # To store the required subpath from a checkpoint.
    allPaths = basefunc(uinpsrc, uinpdest, shrtpath, 0, buses, busstops, busvisited, dp)
    for i in range(len(allPaths)):
        allPaths[i] = [uinpsrc]+allPaths[i]
    minroutelen = 1000
    for i in range(len(allPaths)):
        if minroutelen > len(allPaths[i]):
            minroutelen = len(allPaths[i])
    bestPaths = []
    for i in range(len(allPaths)):
        if len(allPaths[i]) <= minroutelen:
            bestPaths.append(allPaths[i])
    #Remove duplicate paths from list of list returned.
    bestPathsset = set(map(tuple, bestPaths))
    bestPaths = map(list, bestPathsset)
    return bestPaths

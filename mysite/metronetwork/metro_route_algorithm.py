from .models import Graph

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
    grph = {}   #Dictionary of Graph objects.
    for i in range(len(grphobjList)):
        grph[grphobjList[i].name] = grphobjList[i]
    src = grph[uinpsrc]     #Object of Graph type.
    dest = grph[uinpdest]   #Object of Graph type.
    stationvisited = {}    #Marks the stations which are visited.
    stationvisited[src.name]=True
    retval = getallRoutes(src, grph, stationvisited, dest)
    minroutelen = 1000
    for i in range(len(retval)):
        if minroutelen > len(retval[i]):
            minroutelen = len(retval[i])
    bestroutes = []
    for i in range(len(retval)):
        if len(retval[i]) <= minroutelen + 5:
            bestroutes.append(retval[i])
    mindist = 10000
    for i in range(len(bestroutes)):
        dist = 0
        for j in range(len(bestroutes[i])-1):
            u = grph[bestroutes[i][j]]
            v = bestroutes[i][j+1]
            for k in range(len(u.adj_List)):
                if u.adj_List[k] == v:
                    dist = dist + u.dist_List[k]
                    break
        if dist < mindist:
            mindist = dist
    actualdist = str(float(mindist/10.0))
    bestroutes.append([actualdist])
    return bestroutes
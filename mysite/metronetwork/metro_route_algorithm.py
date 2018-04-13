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
    #dp = {}     #To store a subpath from a station.
    stationvisited[src.name]=True
    retval = getallRoutes(src, grph, stationvisited, dest)
    #for i in range(len(retval)):
     #   retval[i] = retval[i].insert(uinpsrc)

    minimum = 1000

    for i in range(len(retval)):
        length = len(retval[i])
        if length < minimum:
            minimum = length
    ans = []
    temp = len(retval)
    for i in range(temp):

        if len(retval[i])  <= minimum + 5:
            ans.append(retval[i])

    minimum = 100000
    for i in range(len(ans)):
        dist = 0
        for j in range(len(ans[i])-1):
            u = grph[ans[i][j]]
            next1 = ans[i][j+1]
            for k in range(len(u.adj_List)):
                if u.adj_List[k] == next1:
                    dist = dist + u.dist_List[k]
                    break

        if dist < minimum:
            minimum = dist
    distance = str(float(minimum/10.0))
    ans.append([distance])
    return ans
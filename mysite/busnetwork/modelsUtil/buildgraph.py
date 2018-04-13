from busnetwork.models import Bus, Busstop, Graph

def main2():
    busstops = Busstop.objects.all()
    for s in busstops:
        obj = Graph()
        obj.name = s.name
        obj.save()
    buses = Bus.objects.all()
    grph = Graph.objects.all()
    for b in buses:
        stps = b.stops
        for i in range(1, len(stps)):
            u = stps[i-1]
            v = stps[i]
            for i in range(len(grph)):
                if grph[i].name == u:
                    if v not in grph[i].adj_list:
                        grph[i].adj_list.append(v)
                        grph[i].save()
                        break
            for i in range(len(grph)):
                if grph[i].name == v:
                    if u not in grph[i].adj_list:
                        grph[i].adj_list.append(u)
                        grph[i].save()
                        break

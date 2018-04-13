from busnetwork.models import Bus, Busstop

def main1():
    buses = Bus.objects.all()
    for b in buses:
        busstops = Busstop.objects.all()
        for s in b.stops:
            flag = False
            for i in range(len(busstops)):
                if busstops[i].name == s:
                    flag = True
                    busstops[i].bus_visit.append(b.id)
                    busstops[i].save()
                    break
            if not flag:
                obj = Busstop()
                obj.name = s
                obj.bus_visit.append(b.id)
                obj.save()

#username: mayadmin
#password: adminpassword

from django.contrib import admin
from .models import Bus, Graph, Busstop

# Register your models here.
admin.site.register(Bus)
admin.site.register(Graph)
admin.site.register(Busstop)

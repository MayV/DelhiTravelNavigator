#username: mayadmin
#password: adminpassword

from django.contrib import admin
from .models import Metro, Graph

# Register your models here.
admin.site.register(Metro)
admin.site.register(Graph)


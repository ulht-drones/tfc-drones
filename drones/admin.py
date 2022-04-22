from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Celula)
admin.site.register(AreaServico)
admin.site.register(Drone)


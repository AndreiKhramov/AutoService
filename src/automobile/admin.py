from automobile.models.automobile import Automobile
from automobile.models.autowork import Autowork
from automobile.models.sparepart import Sparepart
from django.contrib import admin

admin.site.register(Automobile)
admin.site.register(Autowork)
admin.site.register(Sparepart)
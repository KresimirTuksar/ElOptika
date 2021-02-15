from Skladiste.forms import SkladisteCreateForm
from django.contrib import admin

from . models import *
# Register your models here.

class SkladisteCreateAdmin(admin.ModelAdmin):
    list_display = ['kategorija', 'naziv', 'kolicina']
    form = SkladisteCreateForm
    list_filter = ['kategorija']
    search_fields = ['kategorija', 'naziv']

admin.site.register(Skladiste, SkladisteCreateAdmin)
admin.site.register(Kategorija)
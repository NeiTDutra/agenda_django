from django.contrib import admin
from krnl.models import Evento


# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')


admin.site.register(Evento, EventoAdmin)

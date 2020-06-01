from django.contrib import admin
from krnl.models import Evento


# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario',)


admin.site.register(Evento, EventoAdmin)

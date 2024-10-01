from django.contrib import admin
from .models import Evento, Administrador, Atividade


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
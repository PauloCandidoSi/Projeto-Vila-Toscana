from django.contrib import admin
from .models import Evento, Administrador, Atividade


class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    inlines = [AtividadeInline]
    list_display = ('nome', 'descricao')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
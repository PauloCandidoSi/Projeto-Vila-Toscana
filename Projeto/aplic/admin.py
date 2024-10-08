from django.contrib import admin
from .models import Evento, Administrador, Atividade, Endereco, Responsavel, Residente, Categoria, Inscricao, Feedback, Notificacao

class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1
<<<<<<< HEAD
=======

>>>>>>> 3b271dcb329285b93f5416045b9ce35c5e089e73
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    inlines = [AtividadeInline]
    list_display = ('nome', 'descricao')
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Residente)
class residenteAdmin(admin.ModelAdmin):
        list_filter = ('data_nascimento',)
@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep')

@admin.register(Responsavel)
class RespostavelAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'celular', 'telefone_comercial')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = ('status', 'dataHora_inscricao')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'nota', 'dataHora')

@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('mensagem', 'dataEnvio')
import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Evento(models.Model):
    nome = models.CharField(('Nome'), blank=True, max_length=100)
    descricao = models.TextField(('Descrição'), max_length=500)
    imagem = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb':{'width':420, 'height':260, 'crop':True}})

    class Meta:
        verbose_name = ('Evento')
        verbose_name_plural = ('Eventos')


class Usuario(models.Model):
    nome = models.CharField(('Nome'), max_length=100)
    cpf = models.CharField(('CPF'), max_length=100)
    senha = models.CharField(('Senha'), blank=True, max_length=50)
    email = models.EmailField(('E-mail'), blank=True, max_length=100)

    class Meta:
        abstract = True
        verbose_name = ('Usuario')
        verbose_name_plural = ('Usuarios')
        ordering = ['id']

    def __str__(self):
        return self.nome


class Administrador(Usuario):
    cargo = models.CharField(('Cargo'), blank=True, max_length=100)
    telefone = models.CharField(('Telefone'), blank=True, max_length=15)
    data_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))

    class Meta:
        verbose_name = ('Administrador')
        verbose_name_plural = ('Administradores')


class Atividade(models.Model):
    evento = models.ForeignKey(Evento, related_name='Evento', blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(('Nome'), blank=True, max_length=100)
    descricao = models.TextField(('Descrição'), max_length=500)
    data_inicio = models.DateField(('Data de Inicio'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))
    hora_inicio = models.TimeField(('Hora inicio'), blank=True, null=True, help_text=_('Formato HH:MM'))
    local = models.CharField(('Local'), blank=True, max_length=100)
    capacidade = models.IntegerField (('Capacidade'), blank=True, null=True, help_text=_(''))
    imagem = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})

    class Meta:
        verbose_name = ('Atividade')
        verbose_name_plural = ('Atividades')

    def __str__(self):
        return self.nome

import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Evento(models.Model):
    nome = models.TextField(('Nome'), max_length=100)
    descricao = models.TextField(('Descrição'), max_length=500)
    imagem = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb':{'width':420, 'height':260, 'crop':True}})

    class Meta:
        verbose_name = ('Evento')
        verbose_name_plural = ('Eventos')

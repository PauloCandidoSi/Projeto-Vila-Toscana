import uuid

from django.core.exceptions import ValidationError
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

    def __str__(self):
        return self.nome


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

class Categoria(models.Model):
    nome = models.CharField(('Categoria'), blank=True, max_length=50, unique=True)

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    evento = models.ForeignKey(Evento, related_name='Evento', blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(('Nome'), blank=True, max_length=100)
    descricao = models.TextField(('Descrição'), max_length=500)
    data_inicio = models.DateField(('Data de Inicio'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))
    hora_inicio = models.TimeField(('Hora inicio'), blank=True, null=True, help_text=_('Formato HH:MM'))
    local = models.CharField(('Local'), blank=True, max_length=100)
    capacidade = models.IntegerField (('Capacidade'), blank=True, null=True, help_text=_(''))
    imagem = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ('Atividade')
        verbose_name_plural = ('Atividades')

    def __str__(self):
        return self.nome


class Residente(Usuario):
    data_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))
    foto = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})

    class Meta:
        verbose_name = _('Residente')
        verbose_name_plural = _('Residentes')

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    ESTADOS_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    cep = models.CharField(('CEP'), blank=True, max_length=10, help_text=_('Formato 00.000-000'))
    logradouro = models.CharField(('Logradouro'), blank=True, max_length=50)
    numero = models.CharField(('Número'), blank=True, max_length=10)
    complemento = models.CharField(('Complemento'), blank=True, max_length=10)
    bairro = models.CharField(('Bairro'), blank=True, max_length=50)
    cidade = models.CharField(('Cidade'), blank=True, max_length=50)
    estado = models.CharField(('UF'), blank=True, max_length=2, choices=ESTADOS_CHOICES, help_text=_('Formato AA'))
    administrador= models.OneToOneField(Administrador, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Endereço')
        verbose_name_plural = ('Endereços')

    def __str__(self):
        return self.logradouro, self.numero, self.cep, self.complemento, self.bairro, self.cidade, self.estado

class Responsavel(models.Model):
    telefone = models.CharField(('Telefone'), blank=True, max_length=20, help_text=_('Formato (00) 0000-0000'))
    celular = models.CharField(('Celular'), blank=True, max_length=20, help_text=_('Formato (00) 00000-0000'))
    telefone_comercial = models.CharField(('Tel. Comercial'), blank=True, max_length=20, help_text=_('Formato 00) 0000-0000'))
    administador= models.OneToOneField(Administrador, on_delete=models.CASCADE)
    residentes= models.OneToOneField(Residente, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ('Responsável')
        verbose_name_plural = ('Responsáveis')


class Inscricao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    dataHora_inscricao = models.DateTimeField(auto_now_add=True)
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE, blank=True, null=True)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = ('Inscrição')
        verbose_name_plural = ('Inscrições')

    def __str__(self):
        return f"Inscrição de {self.Residente} - {self.status}"


class Feedback(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, blank=True, null=True)
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE, related_name='Feedback', blank=True, null=True)
    comentario = models.TextField(_('Comentario'), max_length=500)
    nota = models.IntegerField(('Nota'), default=0, blank=True, null=True, help_text=_('MAX: 10'))
    dataHora = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'FeedBack'
        verbose_name_plural = ('FeedBacks')

    def __str__(self):
        return f"Feedback para Inscrição {self.inscricao} - Nota: {self.nota}"

    def clean(self):
        # Validação para garantir que a nota não ultrapasse 10
        if self.nota < 0 or self.nota > 10:
            raise ValidationError('A nota deve estar entre 0 e 10.')


class Notificacao(models.Model):

    STATUS_CHOICES = [
        ('nao_lida', 'Não Lida'),
        ('lida', 'Lida'),
    ]

    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, blank=True, null=True)
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField(_('Mensagem'), max_length=500, blank=True, null=True)
    dataEnvio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nao_lida')

    class Meta:
        verbose_name = 'Notificacao'
        verbose_name_plural = ('Notificacoes')

    def __str__(self):
        return f"Notificacao {self.atividade} - Mensagem: {self.mensagem} - status: {self.status}"


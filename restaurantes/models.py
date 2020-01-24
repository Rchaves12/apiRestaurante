from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Restaurantes(models.Model):
    nome = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='fotos/restaurantes', null=True, verbose_name="")
    data_hora_cadastro = models.DateTimeField(default=timezone.now, blank=True, null=False, editable=False)
    ativo = models.BooleanField(default=True)
    enderecos = models.ForeignKey('Enderecos', models.DO_NOTHING, blank=True, null=False)
    telefone = models.CharField(max_length=12)

    class Meta:
        unique_together = (('id', 'id'), )

    def __str__(self):
        return self.nome


class Enderecos(models.Model):
    enderecos = models.CharField(max_length=100, blank=False, null=False)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, blank=False, null=False)
    numero = models.IntegerField()
    data_cadastro = models.DateField(default=timezone.now, blank=True, null=False)
    data_hora_cadastro = models.DateTimeField(default=timezone.now, blank=True, null=False, editable=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.enderecos


class Comentarios(models.Model):
    avaliacao = models.OneToOneField('Avaliacoes', on_delete=models.CASCADE, blank=False, null=False)
    descricao = models.TextField(max_length=255)
    foto = models.ImageField(upload_to='fotos/comentarios', null=True, verbose_name="")
    data_hora_cadastro = models.DateTimeField(default=timezone.now, blank=True, null=False, editable=False)
    ativo = models.BooleanField(default=True)


class Avaliacoes(models.Model):
    restaurante = models.ForeignKey('Restaurantes', on_delete=models.CASCADE, blank=False, null=False)
    avaliacao = models.IntegerField(blank=False, null=False,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    data_hora_cadastro = models.DateTimeField(default=timezone.now, blank=True, null=False, editable=False)
    ativo = models.BooleanField(default=True)


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=5)
    data_hora_cadastro = models.DateTimeField(default=timezone.now, blank=True, null=False, editable=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    data_hora_cadastro = models.DateTimeField(default=timezone.now, blank=True, null=False, editable=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

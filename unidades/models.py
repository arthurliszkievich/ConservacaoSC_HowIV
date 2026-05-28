from django.db import models
from django.conf import settings

class Instituicao(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da Instituição")

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Município")

    class Meta:
        verbose_name = "Município"
        verbose_name_plural = "Municípios"

    def __str__(self):
        return self.nome

class UnidadeConservacao(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='unidades')
    municipios = models.ManyToManyField(Municipio, related_name='unidades')
    
    nome = models.CharField(max_length=200, verbose_name="Nome da Unidade")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    imagem = models.ImageField(upload_to='unidades/', blank=True, null=True, verbose_name="Imagem")
    data_criacao = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        related_name='unidades_criadas', 
        verbose_name="Criado por"
    )

    class Meta:
        verbose_name = "Unidade de Conservação"
        verbose_name_plural = "Unidades de Conservação"

    def __str__(self):
        return self.nome

class Comunicacao(models.Model):
    STATUS_CHOICES = [
        (1, 'Pendente'),
        (2, 'Em Andamento'),
        (3, 'Resolvido'),
    ]
    
    unidade = models.ForeignKey(UnidadeConservacao, on_delete=models.CASCADE, related_name='comunicacoes')
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    email = models.CharField(max_length=150, verbose_name="Email")
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Status")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")

    class Meta:
        verbose_name = "Comunicação"
        verbose_name_plural = "Comunicações"

    def __str__(self):
        return f"{self.titulo} - {self.unidade.nome}"

from django.db import models

UFS = [
        ('SP', 'Sao Paulo'), 
        ('RJ', 'Rio de Janeiro'), 
        ('MG', 'Minas Gerais'), 
        ('BA', 'Bahia')
    ]


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UFS)
        
    def __str__ (self):
        return self.nome


class Interesse(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


# Create your models here.
class Contato(models.Model):

    #opcoes do campo estado civil
    #primeiro valor da tupla é o que vai no banco
    #o segundo é o que mostra na tela
    ESTADO_CIVIS = [
        ('S','Solteiro'), 
        ('C', 'Casado'), 
        ('D', 'Divorciado'), 
        ('V','Viúvo')
        ]
  

    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    DataNascimento = models.DateField(verbose_name="Data de Nascença")
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=UFS)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIS, null=True)
    interesses = models.ManyToManyField(Interesse)


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = ("Pessoa")
        verbose_name_plural = ("Pessoas")

class Telefone(models.Model):
    TIPOS_TELEFONE = [
        ('CEL', 'Celular'),
        ('RES', 'Residencial'), 
        ('COM', 'Comercial'), 
        ('REC', 'Recado')
    ]
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=3, choices=TIPOS_TELEFONE)
    IsWhatsApp = models.BooleanField(verbose_name='Tem WhatsApp?')

    def __str__(self):
        return f'({self.ddd}) {self.numero}'
    

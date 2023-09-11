from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, email, cpf, nome_completo, password):
        if not email:
            raise ValueError('O Email é obrigatório')
        if not cpf:
            raise ValueError('O CPF é obrigatório')
        
        user = self.model(
            email=self.normalize_email(email),
            cpf=cpf,
            nome_completo=nome_completo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, nome_completo, password):
        user = self.create_user(
            email=email,
            cpf=cpf,
            nome_completo=nome_completo,
            password=password,
        )

        user.is_staff = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    is_ativo = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    nome_completo = models.CharField(max_length=255)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'nome_completo']

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Endereco(models.Model):
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=2)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado} {self.cep}'

    class Meta:
        db_table = 'endereco'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class PessoaFisica(Usuario):
    sexo_choices = [
        ('M','MASCULINO'),
        ('F','FEMININO'),
        ('X','NAO INFORMADO')
    ]

    data_nascimento = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=sexo_choices, default='X')
    telefone = models.CharField(max_length=14)

    class Meta:
        db_table = 'pessoa_fisica'
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'


class PessoaJuridica(Usuario):
    cnpj = models.CharField(max_length=18, unique=True)
    descricao = models.TextField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    nome_fantasia = models.CharField(max_length=255)
    nome_razao_social = models.CharField(max_length=255, unique=True)
    telefone = models.CharField(max_length=14)

    class Meta:
        db_table = 'pessoa_juridica'
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'


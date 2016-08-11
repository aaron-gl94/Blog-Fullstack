from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	GENEROS = (
		('H', 'Hombre'),
		('M', 'Mujer'),
		)
	ESTADO = (
		('S', 'Soltero'),
		('C', 'Casado'),
		)
	fecha_nacimiento = models.DateField(null=True,blank=True)
	ocupacion = models.CharField(max_length=140,null=True,blank=True)
	genero = models.CharField(max_length=140,choices=GENEROS, default="M")
	bio = models.TextField(null=True,blank=True)
	civil = models.CharField(max_length=140,choices=ESTADO, default="S")
	User = models.OneToOneField(User)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.User)
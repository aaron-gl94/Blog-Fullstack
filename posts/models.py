from django.db import models 
from django.core.urlresolvers import reverse

class Post(models.Model):
	titulo = models.CharField(max_length=140)
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()
	autor = models.CharField(max_length=140)
	publicado = models.BooleanField(default=False)
	slug = models.SlugField(max_length=500, blank=True, null=True) #Esto es un slung cambia espacios vacios por guiones

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('posts:detalle',args=[self.slug])
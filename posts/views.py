from django.shortcuts import render
from django.views.generic import View
from .models import Post

class ListView(View):
	def get(self, request):
		template_name = 'lista.html'
		posts = Post.objects.all().order_by('titulo')
		context = {
			'posts': posts
			}
		return render(request, template_name, context)


class Home(View):
	def get(self, request):
		template_name = 'home.html'
		return render(request, template_name)

class DetailView(View):
	def get(self, request, slug):
		template_name = 'detalle.html'
		posts = Post.objects.get(slug=slug)
		context = {
			'posts': posts
			}
		return render(request, template_name, context)
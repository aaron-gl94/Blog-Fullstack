from django.shortcuts import render
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.utils.text import slugify

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ListView(View):
	def get(self, request):
		template_name = 'posts/lista.html'
		posts = Post.objects.all().order_by('titulo')
		context = {
			'posts': posts
			}
		return render(request, template_name, context)

"""
class Home(View):
	def get(self, request):
		template_name = 'posts/home.html'
		return render(request, template_name)
"""
class DetailView(View):
	def get(self, request, slug):
		template_name = 'posts/detalle.html'
		posts = Post.objects.get(slug=slug)
		context = {
			'posts': posts
			}
		return render(request, template_name, context)

class FormView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'posts/formpost.html'
		form = PostForm()
		context = {'form':form}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST)
		if form.is_valid():
			nuevo_post = form.save(commit=False)
			nuevo_post.slug = slugify(nuevo_post.titulo)
			nuevo_post.autor = request.user
			nuevo_post.save()
			#La doc de Taggit pide esto:
			form.save_m2m()
			messages.success(request,'Tu post se ha guardado con éxito! ')
			return redirect('posts:lista')
		else:
			messages.error(request,'No se guardo')
			return redirect('posts:nuevo')
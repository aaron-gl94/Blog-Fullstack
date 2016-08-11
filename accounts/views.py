from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Perfil



class PerfilView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name='accounts/perfil.html'
		context={
		}
		return render(request,template_name,context)

class Registro(View):
	def get(self,request):
		template_name='accounts/registro.html'
		form = RegistrationForm()
		context = {
			'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registro.html"
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			# perfil = Profile(instance=new_user)
			new_user.save()
			perfil_nuevo=Perfil()
			perfil_nuevo.user=new_user
			perfil_nuevo.save()
			# perfil = Profile.objects.create(user=new_user)
			return redirect('profile')
		else:
			template_name = "accounts/registro.html"
			context = {
			'form':form
			}
			return render(request,template_name,context)

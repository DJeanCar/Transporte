from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import login, authenticate,logout

class IndexView(TemplateView):
	template_name = 'home/index.html'

	def get_template_names(self):
		if self.request.user.is_authenticated():
			return 'home/index.html'
		else:
			return 'home/login.html'


class LogInView(View):

	def post(self, request, *args, **kwargs):
		acceso = authenticate(username = request.POST['username'], password = request.POST['password'])
		if acceso is not None and acceso.is_active:
			login(request,  acceso)
		return redirect('/')

def LogOut(request):
	logout(request)
	return redirect('/')
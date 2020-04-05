from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import CreateUserForm, CreatePost
from .models import CustomUser
from .emailConfirmation import send_confirmation
from testing.settings import MAIN_ADR


main_adr = MAIN_ADR


class CreateForm(FormView):
	form_class = CreatePost
	success_url = main_adr
	template_name = 'index.html'

	def form_valid(self, form):
		return render(self.request, 'index.html')

	def get(self, request, *args, **kwargs):
		return render(self.request, 'index.html')

	@csrf_exempt
	def post(self, request, *args, **kwargs):
		if not request.user.is_anonymous:
			logout(request)
		return redirect(self.get_success_url())


class CreateUser(FormView):
	form_class = CreateUserForm
	success_url = main_adr
	template_name = 'reg_log.html'

	def form_valid(self, form):
		if not self.request.user.is_authenticated:
			email = form.cleaned_data['email']
			passw = form.cleaned_data['password']
			if 'reg' in self.request.POST:
				try:
					CustomUser.objects.get(email=email)
				except ObjectDoesNotExist:
					send_confirmation(email, passw)
					return redirect(main_adr + 'confirm/')
				else:
					return render(self.request, 'reg_log.html', {'error_r': 'This profile exists. Log in.', 'form': self.get_form_class()})
			user = authenticate(self.request, username=email, password=passw)
			if user is not None:
				login(self.request, user)
			else:
				return render(self.request, self.template_name, {'form': self.form_class, 'error_l': 'Email or password is incorrect'})
		return redirect(self.get_success_url())



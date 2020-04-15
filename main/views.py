from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import CreateUserForm, AccountSettingsForm, CreatePost
from .models import CustomUser, Post
from .emailConfirmation import send_confirmation
from testing.settings import MAIN_ADR
from PIL import Image
import os
from testing.settings import MEDIA_ROOT


main_adr = MAIN_ADR


def logout_(request):
	logout(request)
	return redirect(MAIN_ADR)


class PostList(ListView):
	model = Post
	success_url = main_adr
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		return render(self.request, 'index.html', {'posts': Post.objects.filter(published=True)})


class CreateUser(FormView):
	form_class = CreateUserForm
	success_url = main_adr
	template_name = 'reg_log.html'

	def get(self, request, *args, **kwargs):
		if not request.user.is_anonymous:
			return redirect(self.get_success_url())
		else:
			return render(request, self.template_name, {'form': self.form_class})

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


class AccountSettings(FormView):
	form_class = AccountSettingsForm
	success_url = main_adr
	template_name = 'settings.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return render(request, self.template_name, {'form': self.get_form_class()})
		else:
			return redirect(main_adr)

	def form_valid(self, form):
		passw = form.cleaned_data['old_password']
		user = authenticate(self.request, username=self.request.user.email, password=passw)
		if user is not None:
			avatar = form.cleaned_data['avatar']
			n_password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			current_user = CustomUser.objects.get(email=self.request.user.email)
			if avatar is not None:
				current_user.avatar = form.cleaned_data['avatar']
			if n_password != '':
				current_user.set_password(n_password)
				user_with_new_passw = authenticate(self.request, username=self.request.user.email, password=n_password)
				login(self.request, user_with_new_passw)
			if email != '':
				if self.request.user.email == email:
					return render(self.request, self.template_name, {'form': self.get_form_class(), 'error': "It's your currect email"})
				try:
					CustomUser.objects.get(email=email)
				except ObjectDoesNotExist:
					send_confirmation(email, passw, self.request.user.email)
				else:
					return render(self.request, self.template_name, {'form': self.get_form_class(), 'error': 'Email you entered belong to an another account'})
			current_user.save()
			return redirect(self.get_success_url())
		return render(self.request, self.template_name, {'form': self.get_form_class(), 'error': 'Wrong password'})


class CreatePostView(FormView):
	form_class = CreatePost
	success_url = main_adr + '/post-create/prelook/'
	template_name = 'postform.html'

	def form_valid(self, form):
		if not self.request.user.is_authenticated:
			return redirect(self.get_success_url())
		data = form.cleaned_data
		data['author'] = self.request.user
		post = Post(**data)
		post.save()
		path = os.path.join(MEDIA_ROOT, str(post.img))
		im = Image.open(path)
		x, y = im.size[0], im.size[1]
		y = y / (x / 950) if x > 950 else y
		x = x / (x / 950) if x > 950 else x
		n_size = (int(x), int(y))
		im = im.resize(n_size)  
		im.save(path)
		return render(self.request, 'prelook.html', {'post': post})



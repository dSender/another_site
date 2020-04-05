from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .views import CreateUser, CreateForm


urlpatterns = [
    path('reglog/', CreateUser.as_view()),
    path('', csrf_exempt(CreateForm.as_view())),
    path('confirm/', TemplateView.as_view(template_name='email_confirm.html'))
]



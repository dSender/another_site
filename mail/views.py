from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from testing.settings import MAIN_ADR
from .models import EmailSet
from main.models import CustomUser
from django.db import IntegrityError


class ConfirmPage(TemplateView):

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(EmailSet, **kwargs)
        try:
            us = CustomUser.objects.create_user(email=obj.email, password=obj.passw)
        except IntegrityError:
            return HttpResponse("You have already confirmed your email")
        else:
            login(request, us)
            EmailSet.objects.get(email=obj.email).delete()
        return redirect(MAIN_ADR)

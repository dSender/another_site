from django.contrib import admin
from .models import CustomUser, Post


@admin.register(CustomUser, Post)
class CustomAdmin(admin.ModelAdmin):
    pass
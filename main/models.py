from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import os
from testing.settings import MEDIA_ROOT


class CustomManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


def tmp(instance, file):
    return os.path.join(str(instance.pk), str(file))


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(verbose_name='Avatar', upload_to=tmp)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=CustomUser)
def clear_image_folder(instance, **kwargs):
    path = os.path.join(MEDIA_ROOT, str(instance.pk))
    if kwargs['created'] is not True:
        if len(os.listdir(path)) >= 1:
            file = os.path.split(str(instance.avatar))
            for i in os.listdir(path):
                if i != file[1]:
                    os.remove(os.path.join(path, i))
                else:
                    _path = os.path.join(path, i)
                    im = Image.open(_path)
                    x, y = im.size[0], im.size[1]
                    y = y / (x / 300) if x > 300 else y * (300 / x)
                    x = x / (x / 300) if x > 300 else x * (300 / x)
                    n_size = (int(x), int(y))
                    im = im.resize(n_size)
                    if n_size[1] > 168:
                        im = im.crop((0, 0, x, 168))
                    im.save(_path)
    else:
        os.mkdir(path)



class Post(models.Model):
    title = models.CharField('Title', max_length=32)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

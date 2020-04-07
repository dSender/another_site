from django.db import models


class EmailSet(models.Model):
    url = models.URLField()
    email = models.EmailField()
    passw = models.CharField(max_length=64)
    old_email = models.EmailField()

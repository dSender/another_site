# Generated by Django 3.0.4 on 2020-04-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailset',
            name='passw',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
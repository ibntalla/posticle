# Generated by Django 2.2 on 2019-04-27 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auteur', '0003_auto_20190427_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auteur',
            name='user',
            field=models.OneToOneField(null=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

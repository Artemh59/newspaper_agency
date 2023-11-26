# Generated by Django 4.2.7 on 2023-11-25 15:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_alter_newspaper_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspaper',
            name='redactors',
        ),
        migrations.AddField(
            model_name='newspaper',
            name='redactor',
            field=models.ManyToManyField(related_name='redactor', to=settings.AUTH_USER_MODEL),
        ),
    ]
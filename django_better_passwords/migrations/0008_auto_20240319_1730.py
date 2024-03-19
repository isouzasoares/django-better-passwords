# Generated by Django 3.2.14 on 2024-03-19 17:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_better_passwords', '0007_auto_20240319_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='expiration_day',
            field=models.IntegerField(default=60, verbose_name='Passwords expiration days'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Users that you want to ignore the rule'),
        ),
    ]

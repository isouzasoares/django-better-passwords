# Generated by Django 3.2.14 on 2024-03-19 17:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_better_passwords', '0006_passwordrecord_first_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_day', models.IntegerField(default=60, verbose_name='Expiration days')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Users that you want to ignore the rule')),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2024-02-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_better_passwords', '0002_auto_20240204_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordrecord',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

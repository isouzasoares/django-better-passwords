from django.contrib import admin
from django_better_passwords.models import Configuration


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("expiration_day",)
    autocomplete_fields = ("users",)

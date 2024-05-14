# Generated by Django 5.0.1 on 2024-02-04 22:24


from django.db import migrations


def create_password_record(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    User = apps.get_model("auth", "User")
    PasswordRecord = apps.get_model("django_better_passwords", "PasswordRecord")

    for user in User.objects.all():
        PasswordRecord.objects.create(user=user, password=user.password,
                                      first_login=False)


class Migration(migrations.Migration):
    dependencies = [
        ("django_better_passwords", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_password_record)]

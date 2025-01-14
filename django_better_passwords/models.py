from django.conf import settings
from django.db import models


class PasswordRecord(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="password_records",
        on_delete=models.CASCADE,
        editable=False,
    )

    # max_length django.contrib.auth.base_user.AbstractBaseUser.password
    password = models.CharField("Password hash", max_length=128, editable=False)
    date = models.DateTimeField("Date", auto_now=True, editable=False)
    first_login = models.BooleanField(default=True)

    class Meta:
        get_latest_by = "date"
        ordering = ["-date"]

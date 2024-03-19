from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import (
    resolve,
    reverse,
)
from django.utils import timezone
from django.utils.translation import gettext as _

from django_better_passwords.models import Configuration


class PasswordExpirationMiddleware:
    def __init__(self, get_response):
        self.configuration = Configuration.objects.first()
        self.get_response = get_response
        days = self.configuration.expiration_day \
            if self.configuration \
            else getattr(settings, "DBP_PASSWORD_EXPIRATION_DAYS", 60)
        self.expiration_days = timezone.timedelta(
            days=days
        )

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        resolver_match = resolve(request.path)
        user = request.user

        user_ignore = self.configuration.users.filter(pk=user.pk) \
            if self.configuration else None

        if user.is_authenticated and not user_ignore:
            record = user.password_records

            if ((timezone.now() - record.date) >= self.expiration_days) or (
                record.first_login
            ):
                if (
                    resolver_match.app_name == "admin"
                    and resolver_match.url_name
                    not in (
                        "password_change",
                        "logout",
                    )
                    or not resolver_match.app_name
                    and resolver_match.url_name in ("pages-root", "pages-details-by-slug")
                ):
                    return redirect(
                        reverse(
                            "admin:password_change",
                            current_app=resolver_match.namespace,
                        )
                    )
                elif (
                    hasattr(settings, "DBP_PASSWORD_CHANGE_REDIRECT_URL")
                    and bool(settings.DBP_PASSWORD_CHANGE_REDIRECT_URL)
                    and resolver_match.url_name
                    not in (
                        settings.DBP_PASSWORD_CHANGE_REDIRECT_URL,
                        settings.DBP_LOGOUT_URL,
                    )
                ):

                    return redirect(
                        reverse(
                            settings.DBP_PASSWORD_CHANGE_REDIRECT_URL,
                            current_app=resolver_match.namespace,
                        )
                    )

                if request.method == "GET":
                    message = (
                        _("Update your password to get started.")
                        if record.first_login
                        else _("Your password is at least {} days old and needs to be updated.").format(self.expiration_days.days)
                    )

                    messages.add_message(
                        request,
                        messages.WARNING,
                        message
                    )

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

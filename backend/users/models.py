from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=254,
        unique=True,
        help_text=_("Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    created_at = models.DateTimeField(
        verbose_name=_("Date of creation"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Date of update"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

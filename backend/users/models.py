from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

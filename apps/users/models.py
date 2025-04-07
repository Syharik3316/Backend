from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, verbose_name='О себе')
    website = models.URLField(blank=True, verbose_name='Вебсайт')

    def clean(self):
        super().clean()
        validate_email(self.email)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
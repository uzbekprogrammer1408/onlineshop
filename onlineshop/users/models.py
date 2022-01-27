from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager




class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=4)
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField("Date of Birth", null=True, blank=True)
    card_number = models.BigIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
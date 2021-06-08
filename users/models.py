from typing import Tuple
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
""" Custom User Model """


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "other"),
    ]

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"
    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    ]

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    ]

    avatar = models.ImageField(null=True, blank=True)
    gender = CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, null=True, blank=True
    )
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, null=True, blank=True
    )
    superhost = models.BooleanField(default=False, blank=True)

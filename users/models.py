from django.urls.base import reverse
import rooms
import uuid
from typing import Tuple
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string


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

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return

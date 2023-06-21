from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from my_plant_app.web.validators import capital_letter_validation, only_letters_validation


class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MIN_USERNAME_LEN = 2
    MAX_NAMES_LEN = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LEN),
        )
    )

    first_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        blank=False,
        null=False,
        validators=(
            capital_letter_validation,
        )
    )

    last_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        blank=False,
        null=False,
        validators=(
            capital_letter_validation,
        )
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Plant(models.Model):
    MAX_PLANT_TYPE_LEN = 14
    MAX_NAME_LEN = 20
    MIN_NAME_LEN = 2


    CHOICES = (
        ('OUTDOOR PLANTS', 'Outdoor Plants'),
        ('INDOOR PLANTS', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        max_length=MAX_PLANT_TYPE_LEN,
        choices=CHOICES,
    )

    name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_NAME_LEN),
            only_letters_validation,
        )
    )

    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

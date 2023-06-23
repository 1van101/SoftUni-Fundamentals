from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from my_music_app.web.validators import only_allowed_symbols_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            only_allowed_symbols_validator,
        ]
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )


class Album(models.Model):
    CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False
    )

    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    genre = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        choices=CHOICES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0)
        ]
    )



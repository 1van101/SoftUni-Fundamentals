from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12
    MAX_PASS_LEN = 30
    MAX_NAMES_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_AGE)
        ]
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    MAX_TITLE_LEN = 30
    MAX_CATEGORY_LEN = 15
    MIN_RATING = 0.1
    MAX_RATING = 5
    MIN_LEVEL = 1

    CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
        null=False,
        blank=False,
        unique=True
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LEN,
        null=False,
        blank=False,
        choices=CHOICES
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING)

        ]
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(MIN_LEVEL)
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    summary = models.TextField(
        null=False,
        blank=False
    )

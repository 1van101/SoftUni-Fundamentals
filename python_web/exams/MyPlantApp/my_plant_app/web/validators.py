from django.core.exceptions import ValidationError


def capital_letter_validation(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters_validation(value):
    if not all([x.isalpha() for x in value]):
        raise ValidationError("Plant name should contain only letters!")
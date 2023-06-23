import re

from django.core.exceptions import ValidationError


def only_allowed_symbols_validator(value):
    pattern = '^[A-Za-z0-9_]+$'

    if not re.match(pattern, value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")



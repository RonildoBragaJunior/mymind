
from django.core.validators import RegexValidator

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
"""Tuple containing the available choices for gender representation.
Each choice is represented as a tuple with:
- A short code (like 'M' for Male)
- A descriptive name (like 'Male' for M)
"""

phone_regex = RegexValidator(
    regex=r'^\d{3}-\d{3}-\d{4}$',
    message="Phone number must be in the format: 'XXX-XXX-XXXX'. Only digits are allowed."
)
"""Regex validator for phone numbers.

Ensures that phone numbers follow the format 'XXX-XXX-XXXX', where X is a digit.
If the input doesn't match this format, a validation error will be raised with the provided message.
"""


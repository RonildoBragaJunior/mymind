import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from crm.utils.validators import GENDER_CHOICES, phone_regex


class Customer(models.Model):
    """Represents a customer with associated user details and other personal attributes.
    
    Attributes:
    - uuid: Unique identifier for the customer.
    - user: One-to-one relationship with the Django User model.
    - birth_date: Date of birth of the customer.
    - address: Address of the customer.
    - phone: Phone number of the customer.
    - gender: Gender of the customer (choices defined in GENDER_CHOICES).
    """
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique identifier for the customer
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)  # One-to-one relationship with the Django User model
    birth_date = models.DateField(blank=True, null=True)  # Date of birth of the customer
    address = models.CharField(max_length=200, null=True)  # Address of the customer
    phone = models.CharField(validators=[phone_regex], max_length=12, null=True)  # Phone number of the customer
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)  # Gender of the customer

    def __str__(self):
        return self.user.username  # Return the username as the string representation


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Signal receiver to create an authentication token for a newly created user.
    
    Args:
    - sender: The model class sending the signal.
    - instance: The instance of the model being saved.
    - created: Boolean indicating if the instance is being created or updated.
    - kwargs: Additional keyword arguments.
    """
    if created:
        Token.objects.create(user=instance)  # Create an authentication token for the new user


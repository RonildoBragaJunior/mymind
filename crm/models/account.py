import uuid
from django.db import models
from crm.models import Customer


class Account(models.Model):
    """Represents an account associated with a customer.
    
    Attributes:
    - uuid: Unique identifier for the account.
    - customer: Foreign key to the associated customer.
    """
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique identifier for the account
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)  # Reference to the associated customer


class SubscriptionType(models.Model):
    """Represents a type of subscription with its name, price, and optional description.
    
    Attributes:
    - uuid: Unique identifier for the subscription type.
    - name: Name of the subscription type.
    - price: Price of the subscription type.
    - description: Optional description of the subscription type.
    """
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique identifier for the subscription type
    name = models.CharField(max_length=100)  # Name of the subscription type
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the subscription type
    description = models.TextField(blank=True, null=True)  # Optional description of the subscription type


class Subscription(models.Model):
    """Represents a subscription associated with an account and a subscription type.
    
    Attributes:
    - uuid: Unique identifier for the subscription.
    - account: Foreign key to the associated account.
    - subscription_type: Foreign key to the associated subscription type.
    - start_date: Start date of the subscription.
    - end_date: End date of the subscription.
    - is_active: Boolean indicating if the subscription is currently active.
    """
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique identifier for the subscription
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)  # Reference to the associated account
    subscription_type = models.ForeignKey(to=SubscriptionType, on_delete=models.CASCADE)  # Reference to the associated subscription type
    start_date = models.DateField()  # Start date of the subscription
    end_date = models.DateField()  # End date of the subscription
    is_active = models.BooleanField(default=True)  # Boolean indicating if the subscription is currently active


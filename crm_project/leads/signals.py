from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from customers.models import Customer


@receiver(post_save, sender=Lead)
def create_customer_on_conversion(sender, instance, created, **kwargs):
    """
    Signal to automatically create a Customer when Lead status changes to CONVERTED.
    Prevents duplicate customers by checking email.
    """
    # Only process if lead status is CONVERTED
    if instance.status == Lead.Status.CONVERTED:
        # Check if customer already exists with this email
        existing_customer = Customer.objects.filter(
            email=instance.email,
            is_deleted=False
        ).first()
        
        if not existing_customer:
            # Create new customer from lead data
            Customer.objects.create(
                name=instance.name,
                email=instance.email,
                phone=instance.phone,
                company='',  # Lead doesn't have company field
                status=Customer.Status.CUSTOMER,  # Set status to CUSTOMER
            )

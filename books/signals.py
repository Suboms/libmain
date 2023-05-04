from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from datetime import *


@receiver(post_save, sender=Borrow)
def create_or_update_request(sender, instance, **kwargs):
    try:
        # Try to retrieve an existing PendingRequest instance
        request = PendingRequest.objects.get(book_request=instance)
        request.member = instance.borrower
        request.book = instance.book
        request.save()
    except PendingRequest.DoesNotExist:
        # If no existing PendingRequest instance is found, create a new one
        PendingRequest.objects.create(
            member=instance.borrower, book=instance.book, book_request=instance
        )


@receiver(post_save, sender=PendingRequest)
def update_borrow_return_date(sender, instance, **kwargs):
    if instance.status == "Approved":
        borrow = instance.book_request
        if borrow.due_date is None:
            borrower = borrow.borrower
            if borrower.designation == "Staff":
                borrow.due_date = instance.approval_date + timedelta(days=30)
            else:
                borrow.due_date = instance.approval_date + timedelta(days=14)
            borrow.save()
    elif instance.status == "Declined":
        borrow = instance.book_request
        if borrow.due_date is not None:
            borrow.due_date = None
            borrow.save()

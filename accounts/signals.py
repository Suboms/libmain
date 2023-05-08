from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def generate_user_slug(sender, instance, **kwargs):
    """
    This signal handler generates a slug for the user based on their first and last name
    """
    slugss = slugify(f"{instance.first_name} {instance.last_name}")
    instance.slug = slugss

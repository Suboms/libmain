from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_pic_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".jpg", ".png", ".jpeg", ".hiec"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


def validate_book_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".pdf", ".epub"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


# Create your models here

DESIGNATION = (
    ("Admin", "Admin"),
    ("Staff", "Staff"),
    ("Student", "Student"),
)

LIBUSER = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class User(AbstractUser):
    username = models.CharField(max_length=255, default="", unique=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        default="avatar.png",
        upload_to="images",
        validators=[validate_pic_extension],
    )
    password2 = models.CharField(
        default=None,
        max_length=128,
        verbose_name="Confirm Password",
        null=True,
        blank=True,
    )
    email = models.EmailField(default=None, max_length=255, unique=True)
    designation = models.CharField(
        default=None, choices=DESIGNATION, max_length=255, null=True
    )
    staff_id = models.CharField(
        default=None, max_length=7, null=True, blank=True, verbose_name="Staff Id"
    )
    matric_no = models.CharField(
        default=None, max_length=9, null=True, blank=True, verbose_name="Matric Number"
    )
    lib_user = models.CharField(
        default=None,
        max_length=255,
        choices=LIBUSER,
        blank=True,
        null=True,
        verbose_name="Library User",
    )
    library_id = models.CharField(
        default=None,
        max_length=7,
        blank=True,
        null=True,
        verbose_name="Library Card Id",
    )
    slug = models.SlugField(default="", null=False, blank=True, max_length=255)

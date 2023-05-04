from django.db import models
from accounts.models import *


STATUS = (
    ("Approved", "Approved"),
    ("Declined", "Declined"),
)


class Author(models.Model):
    name = models.CharField(default=None, max_length=255)

    def __str__(self):
        return self.name


class CoAuthor(models.Model):
    name = models.CharField(default=None, max_length=255)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(default=None, max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Books(models.Model):
    book_file = models.FileField(
        upload_to="books",
        validators=[validate_book_extension],
        verbose_name="book",
    )
    title = models.CharField(max_length=255, default=None)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_DEFAULT,
        default="",
    )
    author_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    coauthors = models.ManyToManyField(CoAuthor, blank=True)
    coauthors_name = models.CharField(
        max_length=255, default=None, blank=True, null=True
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_DEFAULT,
        default=None,
        related_name="books_published",
    )
    publisher_name = models.CharField(
        max_length=255, default=None, blank=True, null=True
    )
    genres = models.ManyToManyField(Genre)
    genres_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    isbn = models.CharField(default="", max_length=17)
    edition = models.IntegerField(default=None)

    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Borrow(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    borrower_name = models.CharField(max_length=150, default=None, verbose_name="Name")
    email_address = models.EmailField(
        max_length=150, default=None, verbose_name="E-Mail"
    )
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default="")
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = " Borrow"

    def __str__(self):
        return (str(self.borrower)) + " " + "applied to borrow " + (str(self.book))


class PendingRequest(models.Model):
    book_request = models.ForeignKey(Borrow, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default=None, null=True)
    status = models.CharField(max_length=255, default="", choices=STATUS)
    request_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Pending Request"

    def __str__(self):
        return str(self.member) + " " + "seeking approval to borrow " + str(self.book)


class BookRequest(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


class BookReservation(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_date = models.DateField(auto_now_add=True)

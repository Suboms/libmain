from django import forms
import re
from django.core.exceptions import ValidationError
from .models import *


class BorrowBook(forms.ModelForm):
    class Meta:
        model = Borrow
        exclude = ["borrower", "return_date"]
        widgets = {
            "book": forms.Select(
                attrs={
                    "multiple": True,
                    "class": "form-select",
                    "id": "multiple-select-field",
                }
            ),
            "borrower_name": forms.TextInput(
                attrs={"class": "form-control", "readonly": True}
            ),
            "email_address": forms.EmailInput(
                attrs={"class": "form-control", "readonly": True}
            ),
        }


class ApproveForm(forms.ModelForm):
    class Meta:
        model = PendingRequest
        fields = [
            "id",
            "status",
            "book",
        ]
        widgets = {
            "id": forms.HiddenInput(attrs={"style": "display:none;"}),
            "status": forms.RadioSelect(),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ["author", "coauthors", "publisher", "genres"]
        labels = {
            "author_name": "Author",
            "coauthors_name": "CoAuthor",
            "publisher_name": "Publisher",
            "genres_name": "Genres",
        }
        widgets = {
            "genres_name": forms.TextInput(
                attrs={
                    "list": "genres",
                    "class": "form-control genres-input ",
                    "placeholder": "Enter Genre",
                    "required": True,
                }
            ),
            "book_file": forms.ClearableFileInput(
                attrs={
                    "id": "formFile",
                    "class": "form-control form-control-sm",
                    "placeholder": "Select Book",
                }
            ),
            "author_name": forms.TextInput(
                attrs={
                    "list": "author",
                    "class": "form-control ",
                    "placeholder": "Enter Author Name",
                    "required": True,
                }
            ),
            "coauthors_name": forms.TextInput(
                attrs={
                    "list": "co-author",
                    "id": "co_authors",
                    "class": "form-control coauthor-name",
                    "placeholder": "Enter Co-authors Name",
                }
            ),
            "publisher_name": forms.TextInput(
                attrs={
                    "list": "publisher",
                    "class": "form-control ",
                    "placeholder": "Enter Publisher",
                    "required": True,
                }
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control ", "placeholder": "Enter Title"}
            ),
            "edition": forms.NumberInput(
                attrs={"class": "form-control ", "placeholder": "Enter Edition"}
            ),
            "isbn": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "data-mask": "978-3-16-148410-0",
                    "placeholder": "978-3-16-148410-0",
                    "id": "isbn-input",
                    "oninput": "formatISBN()",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Description",
                    "rows": 15,
                    "cols": 60,
                }
            ),
        }

    def clean_author_name(self):
        author = self.cleaned_data.get("author_name")
        if any(char.isdigit() for char in author):
            raise ValidationError("Invalid Author's Name")
        elif author and re.search("[!@#$%^&*()_+}{\":?><|\\\/,/;'[\]]", author):
            raise ValidationError("Invalid Author's Name")
        return author

    def clean_coauthors_name(self):
        coauthors = self.cleaned_data.get("coauthors_name")
        if coauthors is not None and any(char.isdigit() for char in coauthors):
            raise ValidationError("Invalid CoAuthor's Name")
        elif coauthors and re.search("[!@#$%^&*()_+}{\":?><|\\\/,./;'[\]]", coauthors):
            raise ValidationError("Invalid CoAuthor's Name")
        return coauthors

    def clean_publisher_name(self):
        publisher = self.cleaned_data.get("publisher_name")
        if any(char.isdigit() for char in publisher):
            raise ValidationError("Invalid Publisher's Name")
        elif publisher and re.search("[!@#$%^&*()_+}{\":?><|\\\/,./;'[\]]", publisher):
            raise ValidationError("Invalid Publisher's Name")
        return publisher

    def clean_genres_name(self):
        genres = self.cleaned_data.get("genres_name")
        if any(char.isdigit() for char in genres):
            raise ValidationError("Invalid Genre's Name")
        elif genres and re.search("[!@#$%^&*()_+}{\":?><|\\\/,./;'[\]]", genres):
            raise ValidationError("Invalid Genre's Name")
        return genres

    def clean_isbn(self):
        isbn = self.cleaned_data.get("isbn")
        if len(isbn) != 10 and len(isbn) != 13:
            raise forms.ValidationError("Invalid ISBN number")
        elif isbn is not None and Books.objects.filter(isbn=isbn).exists():
            raise forms.ValidationError("Invalid ISBN number")
        return isbn

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        edition = cleaned_data.get("edition")
        if (
            title is not None
            and Books.objects.filter(title__iexact=title, edition=edition).exists()
        ):
            raise ValidationError("A book with this title and edition already exists.")
        return cleaned_data

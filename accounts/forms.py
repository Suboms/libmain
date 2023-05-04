from django import forms
from django.contrib.auth.forms import *
from accounts.models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "staff_id",
            "matric_no",
            "library_id",
            "designation",
            "lib_user",
        ]
        help_texts = {
            "username": None,
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "is_staff": "Administrative Account",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mikey",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Chinedu",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Oladapo Dikko",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "abc@example.com",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control password-toggle",
                    "placeholder": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
                    "autocomplete": "on",
                    "pattern": "(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~!@#$%^&*()_]).{8,}",
                    "required": False,
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
                    "autocomplete": "on",
                }
            ),
            "staff_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "PFAS123",
                    "id": "staff_id",
                }
            ),
            "matric_no": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "180591001",
                    "id": "matric_no",
                }
            ),
            "library_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "LIB1234",
                    "id": "library_id",
                }
            ),
            "designation": forms.RadioSelect(
                attrs={
                    "class": "form-check-input",
                    "id": "designation",
                }
            ),
            "lib_user": forms.RadioSelect(
                attrs={
                    "class": "form-check-input",
                    "id": "library_user",
                }
            ),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username is not None and User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken.")
        return username.lower() if username else None

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email is not None and User.objects.filter(email=email).exists():
            raise ValidationError("Email already taken")
        return email

    def clean_matric_no(self):
        matric_no = self.cleaned_data.get("matric_no")
        if matric_no is not None:
            if len(matric_no) < 9:
                raise ValidationError("Invalid matric number")
            try:
                return int(matric_no)
            except ValueError:
                raise ValidationError("Invalid matric number")
        return None

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get("staff_id")
        if staff_id is not None and not re.match(
            "^(pfas|pfss|pfjs)\d{3}$", str(staff_id)
        ):
            raise ValidationError("Invalid Staff Id")

        return staff_id

    def clean_library_id(self):
        library_id = self.cleaned_data.get("library_id")
        if library_id is not None and not re.match("^(lib|LIB)\d{4}$", str(library_id)):
            raise ValidationError("Invalid Library Card Id.")
        return library_id

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise ValidationError("Password Mismatch")
        elif password and len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        elif password and not re.search("[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter")
        elif password and not re.search("[a-z]", password):
            raise ValidationError("Password must contain at least one lowercase letter")
        elif password and not re.search("[0-9]", password):
            raise ValidationError("Password must contain at least one digit")
        elif password and not re.search(
            "[!@#$%^&*()_+}{\":?><|\\\/,./;'[\]]", password
        ):
            raise ValidationError(
                "Password must contain at least one special character"
            )

        staff_id = cleaned_data.get("staff_id")
        matric_no = cleaned_data.get("matric_no")
        library_id = cleaned_data.get("library_id")

        if staff_id is not None and User.objects.filter(staff_id=staff_id).exists():
            raise ValidationError("Staff Id already exists")

        if matric_no is not None and User.objects.filter(matric_no=matric_no).exists():
            raise ValidationError("Matric No already exists")

        if (
            library_id is not None
            and User.objects.filter(library_id=library_id).exists()
        ):
            raise ValidationError("Library Id already exists")

        return cleaned_data


class AdminSignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "staff_id",
            "matric_no",
            "library_id",
            "designation",
            "lib_user",
        ]
        help_texts = {
            "username": None,
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "is_staff": "Administrative Account",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mikey",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Chinedu",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Oladapo Dikko",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "abc@example.com",
                }
            ),
            "staff_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "PFAS123",
                    "id": "staff_id",
                }
            ),
            "matric_no": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "180591001",
                    "id": "matric_no",
                }
            ),
            "library_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "LIB1234",
                    "id": "library_id",
                }
            ),
            "designation": forms.RadioSelect(
                attrs={
                    "class": "form-check-input",
                    "id": "designation",
                }
            ),
            "lib_user": forms.RadioSelect(
                attrs={
                    "class": "form-check-input",
                    "id": "library_user",
                }
            ),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username is not None and User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken.")
        return username.lower() if username else None

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email is not None and User.objects.filter(email=email).exists():
            raise ValidationError("Email already taken")
        return email

    def clean_matric_no(self):
        matric_no = self.cleaned_data.get("matric_no")
        if matric_no is not None:
            if len(matric_no) < 9:
                raise ValidationError("Invalid matric number")
            try:
                return int(matric_no)
            except ValueError:
                raise ValidationError("Invalid matric number")
        return None

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get("staff_id")
        if staff_id is not None and not re.match(
            "^(pfas|pfss|pfjs)\d{3}$", str(staff_id)
        ):
            raise ValidationError("Invalid Staff Id")

        return staff_id

    def clean_library_id(self):
        library_id = self.cleaned_data.get("library_id")
        if library_id is not None and not re.match("^(lib|LIB)\d{4}$", str(library_id)):
            raise ValidationError("Invalid Library Card Id.")
        return library_id

    def clean(self):
        cleaned_data = super().clean()
        staff_id = cleaned_data.get("staff_id")
        matric_no = cleaned_data.get("matric_no")
        library_id = cleaned_data.get("library_id")

        if staff_id is not None and User.objects.filter(staff_id=staff_id).exists():
            raise ValidationError("Staff Id already exists")

        if matric_no is not None and User.objects.filter(matric_no=matric_no).exists():
            raise ValidationError("Matric No already exists")

        if (
            library_id is not None
            and User.objects.filter(library_id=library_id).exists()
        ):
            raise ValidationError("Library Id already exists")

        return cleaned_data


class Signin(forms.Form):
    username = forms.CharField(
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "dubsy",
                "required": True,
                "aria-describedby": "emailHelp",
            }
        ),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "required": True,
                "placeholder": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
            }
        ),
    )


class Profile(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "matric_no",
            "library_id",
            "lib_user",
            "staff_id",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mikey",
                    "readonly": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ex@example.com",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Chinedu",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Oladapo Dikko",
                }
            ),
            "matric_no": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "180591001",
                }
            ),
            "library_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "LIB1234",
                    "id": "library_id",
                }
            ),
            "lib_user": forms.RadioSelect(
                attrs={
                    "id": "lib_user",
                    "class": "form-check-input",
                }
            ),
            "staff_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "PFAS123",
                }
            ),
            "avatar": forms.FileInput(attrs={"class": "form-control form-control-sm"}),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if (
            username is not None
            and self.instance.username != username
            and User.objects.filter(username=username).exists()
        ):
            raise ValidationError("Username already taken.")
        return username.lower() if username else None

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if (
            email is not None
            and self.instance.email != email
            and User.objects.filter(email=email).exists()
        ):
            raise ValidationError("Email already taken")
        return email

    def clean_matric_no(self):
        matric_no = self.cleaned_data.get("matric_no")
        if (
            matric_no is not None
            and self.instance.matric_no != matric_no
            and User.objects.filter(matric_no=matric_no).exists()
        ):
            raise ValidationError("Matric No already exists")
        elif matric_no is not None:
            if len(matric_no) < 9:
                raise ValidationError("Invalid matric number")
            try:
                return int(matric_no)
            except ValueError:
                raise ValidationError("Invalid matric number")
        return matric_no

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get("staff_id")
        if staff_id is not None:
            if not re.match("^(pfas|pfss|pfjs|PFAS|PFSS|PFJS)\d{3}$", str(staff_id)):
                raise ValidationError("Invalid Staff Id")
            elif (
                staff_id is not None
                and self.instance.staff_id != staff_id
                and User.objects.filter(staff_id=staff_id).exists()
            ):
                raise ValidationError("Staff Id already exists")
        return staff_id

    def clean_library_id(self):
        library_id = self.cleaned_data.get("library_id")
        if library_id is not None:
            if not re.match("^(lib|LIB)\d{4}$", str(library_id)):
                raise ValidationError("Invalid Staff Id")
            elif (
                library_id is not None
                and self.instance.library_id != library_id
                and User.objects.filter(library_id=library_id).exists()
            ):
                raise ValidationError("Library Id already exists")
        return library_id

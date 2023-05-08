from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import logout, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import *
import random
import string

# Define a function to generate a random string of 6 characters
User = get_user_model()
# Create your views here.


def generate_random_string():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


random_string = generate_random_string()


def index(request):
    return render(request, "index.html", {})


def signup(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form = AdminSignUp(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username").lower()
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken.")
                else:
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.first_name = user.first_name.lower()
                    user.last_name = user.last_name.lower()
                    user.slug = slugify(
                        f"{user.first_name} {user.last_name} {random_string}")
                    user.email = user.email.lower()
                    user.set_password(
                        f"@{user.first_name.title()}{user.last_name.title()}123"
                    )
                    user.password2 = None
                    if user.staff_id:
                        user.staff_id = user.staff_id.upper()
                    if user.library_id:
                        user.library_id = user.library_id.upper()
                    if user.designation == "Admin":
                        user.is_staff = True
                    user.save()
                    login(request, user)
                    messages.success(
                        request, "Account created successfully for " + username
                    )
                    return redirect("signin")
        else:
            form = AdminSignUp()
        return render(request, "accounts/register.html", {"form": form})
    else:
        if request.method == "POST":
            form = SignUp(request.POST)
            if form.is_valid():
                next_url = request.POST.get("next", "/")
                username = form.cleaned_data.get("username").lower()
                password = form.cleaned_data.get("password")
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken.")
                else:
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.first_name = user.first_name.lower()
                    user.last_name = user.last_name.lower()
                    user.slug = slugify(
                        f"{user.first_name} {user.last_name} {random_string}")
                    user.email = user.email.lower()
                    user.set_password(password)
                    user.password2 = None
                    if user.staff_id:
                        user.staff_id = user.staff_id.upper()
                    if user.library_id:
                        user.library_id = user.library_id.upper()
                    if user.designation == "Admin":
                        user.is_staff = True
                    user.save()
                    login(request, user)
                    messages.success(
                        request, "Account created successfully for " + username
                    )
                    return redirect(next_url)
        else:
            form = SignUp()
        return render(
            request,
            "accounts/register.html",
            {"form": form, "next": request.GET.get("next", "/")},
        )


def signin(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            next_url = request.POST.get("next", "/")

            user = User.objects.filter(username=username.lower()).exists()
            mail = User.objects.filter(email=username.lower()).exists()
            if user:
                get_user = User.objects.filter(username=username.lower())
                check_pass = check_password(password, get_user[0].password)
                if not check_pass:
                    messages.error(request, "Invalid Credentials")
                    return redirect(signin)
                else:
                    login(request, get_user[0])
                    return redirect(next_url)
            elif mail:
                get_user = User.objects.filter(email=username.lower())
                check_pass = check_password(password, get_user[0].password)
                if not check_pass:
                    messages.error(request, "Invalid Credentials")
                    return redirect(signin)
                else:
                    login(request, get_user[0])
                    return redirect(next_url)
            else:
                messages.error(request, "Invalid Credentials")
                return redirect(signin)
    else:
        form = Signin()
        return render(
            request,
            "accounts/login.html",
            {"form": form, "next": request.GET.get("next", "/")},
        )


def signout(request):
    logout(request)
    return redirect(index)


@login_required
def profile(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.user.is_superuser:
        if request.method == "POST":
            form = Profile(request.POST, request.FILES, instance=user)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.first_name = profile.first_name.lower()
                profile.last_name = profile.last_name.lower()
                profile.slug = slugify(
                    f"{profile.first_name} {profile.last_name} {random_string}")
                profile.email = profile.email.lower()
                if profile.library_id:
                    profile.library_id = profile.library_id.upper()
                elif profile.lib_user == "No":
                    profile.library_id = None
                profile.save()
                return redirect(index)
        else:
            form = Profile(instance=user)
        return render(request, "accounts/profile.html", {"form": form, "user": user})
    else:
        pass


@login_required
def settings(request, slug):
    user = get_object_or_404(User, slug=slug)
    if request.method == "POST":
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.first_name = profile.first_name.lower()
            profile.last_name = profile.last_name.lower()
            profile.slug = slugify(
                f"{profile.first_name} {profile.last_name} {random_string}")
            profile.email = profile.email.lower()
            if profile.library_id:
                profile.library_id = profile.library_id.upper()
            elif profile.lib_user == "No":
                profile.library_id = None
            profile.save()
            return redirect(index)
    else:
        form = Profile(instance=user)
    return render(request, "accounts/profile.html", {"form": form, "user": user})


def student_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        students = User.objects.filter(designation="Student")
        context = {"students": students}
        return render(request, "accounts/studentlist.html", context)


def delete_student(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        students = User.objects.filter(id=pk)
        students.delete()
        return redirect(student_list)


def staff_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        staffs = User.objects.filter(designation="Staff")
        context = {"staffs": staffs}
        return render(request, "accounts/stafflist.html", context)


def delete_staff(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        staffs = User.objects.filter(id=pk)
        staffs.delete()
        return redirect(staff_list)


def admin_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        admins = User.objects.filter(designation="Admin")
        context = {"admins": admins}
        return render(request, "accounts/adminlist.html", context)


def delete_admin(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        admins = User.objects.filter(id=pk)
        admins.delete()
        return redirect(admin_list)


def manage_users(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, "accounts/usermanagement.html", {})

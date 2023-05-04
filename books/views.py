from django.shortcuts import render, redirect
from accounts.views import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.forms import *


@login_required
def borrow(request):
    if request.user.staff_id is None and request.user.library_id is None:
        messages.error(request, "you cannot view this page")
        return redirect(index)
    else:
        if request.method == "POST":
            form = BorrowBook(request.POST)
            if form.is_valid():
                borrower_name = form.cleaned_data["borrower_name"]
                email_address = form.cleaned_data["email_address"]
                books = request.POST.getlist("book")
                if request.user.designation == "Staff":
                    if (
                        Borrow.objects.filter(borrower=request.user).count()
                        + len(books)
                        > 5
                    ):
                        messages.error(
                            request, "You cannot apply to borrow more than 5 books"
                        )
                    else:
                        for book_id in books:
                            book = Books.objects.get(id=book_id)
                            Borrow.objects.get_or_create(
                                borrower=request.user,
                                book=book,
                                borrower_name=borrower_name,
                                email_address=email_address,
                            )
                elif request.user.designation == "Student":
                    if (
                        Borrow.objects.filter(borrower=request.user).count()
                        + len(books)
                        > 3
                    ):
                        messages.error(
                            request, "You cannot apply to borrow more than 3 books"
                        )
                    else:
                        for book_id in books:
                            book = Books.objects.get(id=book_id)
                            Borrow.objects.get_or_create(
                                borrower=request.user,
                                book=book,
                                borrower_name=borrower_name,
                                email_address=email_address,
                            )
                return redirect(index)
        else:
            form = BorrowBook(
                initial={
                    "borrower_name": request.user.first_name
                    + " "
                    + request.user.last_name,
                    "email_address": request.user.email,
                }
            )
        return render(request, "books/borrow.html", {"form": form})


def notfound(request):
    return render(request, "404.html", {})


@login_required
def pending(request):
    if not request.user.is_superuser:
        return redirect(notfound)
    else:
        users = PendingRequest.objects.filter(
            member__isnull=False).distinct("member")
        return render(request, "books/request.html", {"users": users})


@login_required
def addbook(request):
    if not request.user.is_superuser:
        return redirect(notfound)
    else:
        books = Books.objects.all()
        genres = Genre.objects.all()
        authors = Author.objects.all()
        coauthors = CoAuthor.objects.all()
        publishers = Publisher.objects.all()
        if request.method == "POST":
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                book = request.FILES.get("book_file")
                title = request.POST.get("title")
                isbn = request.POST.get("isbn")
                description = request.POST.get("description")
                genres_name = request.POST.getlist("genres_name")
                author_name = request.POST.get("author_name")
                co_authors = request.POST.getlist("coauthors_name")
                publisher_name = request.POST.get("publisher_name")
                author_name, created = Author.objects.get_or_create(
                    name=author_name.title()
                )
                publisher, created = Publisher.objects.get_or_create(
                    name=publisher_name.title()
                )

                book = Books.objects.create(
                    isbn=isbn,
                    title=title.title(),
                    publisher=publisher,
                    edition=request.POST.get("edition"),
                    author=author_name,
                    book_file=book,
                    description=description,
                )
                for genre in genres_name:
                    genre, created = Genre.objects.get_or_create(
                        name=genre.lower())
                    book.genres.add(genre)
                if co_authors:
                    for co_author in co_authors:
                        coauthor, created = CoAuthor.objects.get_or_create(
                            name=co_author.title()
                        )
                        book.coauthors.add(coauthor)
                return redirect(addbook)
        else:
            form = BookForm()
        context = {
            "form": form,
            "genres": genres,
            "authors": authors,
            "publishers": publishers,
            "books": books,
            "coauthors": coauthors,
        }
        return render(request, "books/addbook.html", context)


@login_required
def approve(request, pk):
    if not request.user.is_superuser:
        return redirect(notfound)
    else:
        member = get_object_or_404(User, id=pk)
        pending_requests = PendingRequest.objects.filter(member=member)
        PendingRequestFormSet = modelformset_factory(
            PendingRequest, form=ApproveForm, extra=0
        )
        if request.method == "POST":
            formset = PendingRequestFormSet(
                request.POST, queryset=pending_requests)
            if formset.is_valid():
                for form in formset:
                    if form.cleaned_data.get("approved"):
                        form.instance.approved = True
                        form.instance.declined = False
                        form.instance.save()
                    else:
                        form.instance.approved = False
                        form.instance.declined = True
                        form.instance.save()
        else:
            formset = PendingRequestFormSet(queryset=pending_requests)
        context = {"formset": formset, "member": member}
        return render(request, "books/approve.html", context)


@login_required
def request_list(request):
    if not request.user.is_superuser:
        return redirect(notfound)
    else:
        users = User.objects.all().prefetch_related(
            Prefetch(
                "pendingrequest_set",
                queryset=PendingRequest.objects.all().order_by("request_date"),
            )
        )
        user_requests = {}
        for user in users:
            pending_requests = user.pendingrequest_set.all()
            approved_requests = pending_requests.filter(status="Approved")
            declined_requests = pending_requests.filter(status="Declined")

            user_requests[user.username] = {
                "approved_requests": approved_requests,
                "declined_requests": declined_requests,
            }

        context = {"user_requests": user_requests}
        return render(request, "books/requestlist.html", context)


def books_list(request):
    books = Books.objects.all()
    context = {"books": books}
    return render(request, "books/booklist.html", context)


def delete_book(request, pk):
    books = Books.objects.filter(id=pk)
    books.delete()
    return redirect(books_list)


def manage_books(request):
    return render(request, "books/bookmanagement.html", {})

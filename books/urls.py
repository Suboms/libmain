from django.urls import path

from . import views

urlpatterns = [
    path("borrow/", views.borrow, name="borrow"),
    path("pending/", views.pending, name="pending"),
    path("approve/<int:pk>/", views.approve, name="approve"),
    path("404/", views.notfound, name="404"),
    path("books/create/", views.addbook, name="addbook"),
    path("request-list/", views.request_list, name="request-list"),
    path("books/list/", views.books_list, name="books-list"),
    path("remove-book/<int:pk>/", views.delete_book, name="delete-book"),
    path("books/", views.manage_books, name="manage-books"),
    
]

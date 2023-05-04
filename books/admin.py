from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Genre)


class BorrowAdmin(admin.ModelAdmin):
    readonly_fields = (
        "borrow_date",
        "due_date",
    )
    ordering = ("id",)


class PendingRequestAdmin(admin.ModelAdmin):
    readonly_fields = (
        "approval_date",
        "request_date",
    )
    list_filter = ("book",)
    ordering = ("id",)


class BookAdmin(admin.ModelAdmin):
    list_filter = (
        "genres",
        "author",
        "coauthors",
    )
    readonly_fields = ("created_at",)


admin.site.register(Books, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(PendingRequest, PendingRequestAdmin)
admin.site.register(Author)
admin.site.register(BookRequest)
admin.site.register(CoAuthor)
admin.site.register(BookReservation)
admin.site.register(Publisher)

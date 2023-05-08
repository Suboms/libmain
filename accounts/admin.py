from django.contrib import admin
from accounts.models import *


class UserAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_filter = ("designation",)
    list_display = (
        "first_name",
        "last_name",
        "email",
        "date_joined",
    )
    prepopulated_fields = {"slug": ("first_name", "last_name")}


admin.site.register(User, UserAdmin)

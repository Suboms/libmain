from django.contrib import admin
from accounts.models import *


class UserAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_filter = ("designation",)


admin.site.register(User, UserAdmin)

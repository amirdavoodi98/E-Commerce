from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdminUser(admin.ModelAdmin):
    list_display = ('id', 'username')

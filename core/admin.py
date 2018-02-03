from django.contrib import admin

from .models import UserData


# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievements', 'position')


# Admin Registers
admin.site.register(UserData, UserDataAdmin)

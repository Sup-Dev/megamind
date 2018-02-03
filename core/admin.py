from django.contrib import admin

from .models import UserData

from .models import Meeting
from .models import Speech
from .models import Role

from .models import Winners


# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievements', 'position')


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'club_name')


class SpeechAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'speaker', 'number', 'evaluator')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'role_player', 'role')


class WinnerAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'category')


# Admin Registers
admin.site.register(UserData, UserDataAdmin)

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Speech, SpeechAdmin)
admin.site.register(Role, RoleAdmin)

admin.site.register(Winners, WinnerAdmin)

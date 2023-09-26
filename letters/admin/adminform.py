from django.contrib import admin
from .models import IncomingLetter, OutgoingLetter

@admin.register(IncomingLetter)
class IncomingLetterAdmin(admin.ModelAdmin):
    form = IncomingLetterAdminForm

@admin.register(OutgoingLetter)
class OutgoingLetterAdmin(admin.ModelAdmin):
    form = OutgoingLetterAdminForm

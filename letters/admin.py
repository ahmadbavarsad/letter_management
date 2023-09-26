from django.contrib import admin
from jalali_date import date2jalali, datetime2jalali
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import IncomingLetter, OutgoingLetter
from .forms import IncomingLetterAdminForm, OutgoingLetterAdminForm


@admin.register(IncomingLetter)
class IncomingLetterAdmin(admin.ModelAdmin):
    form = IncomingLetterAdminForm

@admin.register(OutgoingLetter)
class OutgoingLetterAdmin(admin.ModelAdmin):
    form = OutgoingLetterAdminForm

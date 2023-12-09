from django.contrib import admin
from jalali_date import date2jalali, datetime2jalali
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import *
from .forms import IncomingLetterAdminForm, OutgoingLetterAdminForm


admin.sites.AdminSite.site_header = "پنل مدیریت نامه های کاردانی"


@admin.register(IncomingLetter)
class IncomingLetterAdmin(admin.ModelAdmin):
    form = IncomingLetterAdminForm


@admin.register(OutgoingLetter)
class OutgoingLetterAdmin(admin.ModelAdmin):
    form = OutgoingLetterAdminForm



admin.site.register(IncomingCategoryLetter)
admin.site.register(OutgoingCategoryLetter)
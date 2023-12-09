from django.shortcuts import render, redirect, get_object_or_404
from django_jalali.db import models as jmodels
from jalali_date.fields import JalaliDateField

from django.http import FileResponse
from .models import *

def books_view(request):
    books = BookName.objects.all()
    return render(request, 'books.html', {'books': books})

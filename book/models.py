from django.db import models
from django_jalali.db import models as jmodels
from jalali_date.fields import JalaliDateField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):  
    WriterName = models.CharField(max_length=30, verbose_name='نام نویسنده')  
  
    class Meta:
        db_table = 'author'
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'
    def __unicode__(self):
        return self.WriterName
    def __str__(self):
        return self.WriterName
     

class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'مرد'),
        ('F', 'زن'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

     
class BookCategory(models.Model):
   BookName = models.CharField(max_length=64, verbose_name='دسته بندی موضوعی')

   class Meta:
        db_table = 'book_category'
        verbose_name = 'دسته بندی موضوعی'
        verbose_name_plural = 'دسته بندی موضوعی'
   def __unicode__(self):
        return self.BookName
   def __str__(self):
        return self.BookName


class PublisherCategory(models.Model):
   PublisherName = models.CharField(max_length=64, verbose_name='انتشارات')

   class Meta:
        db_table = 'publisher_category'
        verbose_name = 'انتشارات'
        verbose_name_plural = 'انتشاراتی ها'
   def __unicode__(self):
        return self.PublisherName
   def __str__(self):
        return self.PublisherName


class BookName(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان کتاب')
    publisher = models.ForeignKey(PublisherCategory, on_delete=models.CASCADE, verbose_name='انتشارات')
    Category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name='دسته بندی موضوعی')
    slug = models.SlugField(max_length = 250,unique_for_date='publish', verbose_name='آدرس انگلیسی')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نویسنده')
    BookImage = models.FileField(upload_to='BookImage/', 
    validators=[FileExtensionValidator(allowed_extensions=['jpg'], message='پسوندهای مجاز jpg می باشد')], verbose_name=('تصویر کتاب (jpg)')
)
    BookDL = models.FileField(upload_to='download/Category/Books',
    validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='پسوندهای مجاز PDF می باشد')], verbose_name=('آپلود کتاب (PDF)')
)
    body = models.TextField(verbose_name='درباره نویسنده')
    publish = models.DateTimeField(default=timezone.now, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    
    class Meta:
        db_table = 'book_name'
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title



class BookID(models.Model):
    IdNumber = models.CharField(max_length=10, verbose_name='کد کتاب')

    class Meta:
        db_table = 'id_Number'
        verbose_name = 'کد کتاب'
        verbose_name_plural = 'کد کتاب ها'
    def __unicode__(self):
        return self.IdNumber
    def __str__(self):
        return self.IdNumber
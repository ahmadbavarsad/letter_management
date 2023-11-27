from django.db import models
from django_jalali.db import models as jmodels
from jalali_date.fields import JalaliDateField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify


OPTIONS = (
    ('COOL', 'COOL'),
    ('WARM', 'WARM'),
)
class WriterName(models.Model):
     options = models.CharField(max_length=20, choices=OPTIONS, default=None,blank=True, null=True)

class Article(models.Model):
    STATUS = Choices('draft', 'published')
    status = models.CharField(choices=STATUS, default=STATUS.draft, max_length=20)


class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    writer_name = models.Choices(WriterName,)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    slug = models.SlugField(db_column='slug', blank=False, unique=True, allow_unicode=True,verbose_name='نام دلخواه')

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


class IncomingCategoryLetter(models.Model):
    SahebanName = models.CharField(max_length=100, unique=True, verbose_name='صاحبان نامه ها')

    class Meta:
        db_table = 'IncomingCategoryLetter'
        verbose_name = 'صاحبان نامه'
        verbose_name_plural = 'صاحبان نامه'
    def __unicode__(self):
        return self.SahebanName
    def __str__(self):
        return self.SahebanName
    
#نامه وارده
class IncomingLetter(models.Model):
    category = models.ManyToManyField(IncomingCategoryLetter, verbose_name='صاحبان نامه ها')
    subject = models.CharField(max_length=50, verbose_name='عنوان نامه')
    IncomingLetterNumber = models.CharField(max_length=20, verbose_name='شماره نامه')
    document = models.FileField(upload_to='incoming_letters/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('pdfیا jpgتصویرنامه')
)
    class Meta:
        db_table = 'IncomingLetter'
        verbose_name = 'نامه وارده'
        verbose_name_plural = 'نامه وارده'
    def __unicode__(self):
        return self.IncomingLetterNumber
    def __str__(self):
        return self.IncomingLetterNumber

class OutgoingCategoryLetter(models.Model):
    SahebanName = models.CharField(max_length=100, unique=True, verbose_name='صاحبان نامه ها')

    def __str__(self):
        return self.SahebanName

#نامه صادره
class OutgoingLetter(models.Model):
    category = models.ManyToManyField(OutgoingCategoryLetter, verbose_name='صاحبان نامه ها')
    subject = models.CharField(max_length=50, verbose_name='عنوان نامه')
    OutgoingLetterNumber = models.CharField(max_length=20, verbose_name='شماره نامه')
    document = models.FileField(upload_to='outgoing_letters/', 
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('تصویرنامه (pdf یا jpg)')
,blank=True)
    OutgoingDraft = models.FileField(upload_to='outgoing_letters/draft',
    validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'], message='پسوندهای مجاز doc و docx می باشد')], verbose_name=('فایل ورد نامه (doc یا docx)')
)
    
    def __str__(self):
        return self.OutgoingLetterNumber
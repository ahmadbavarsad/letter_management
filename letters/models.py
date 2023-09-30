from django.db import models
from django_jalali.db import models as jmodels
from jalali_date.fields import JalaliDateField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

class IncomingCategoryLetter(models.Model):
    SahebanName = models.CharField(max_length=100, unique=True, verbose_name='صاحبان نامه ها')

    def __str__(self):
        return self.SahebanName

#نامه وارده
class IncomingLetter(models.Model):
    category = models.ManyToManyField(IncomingCategoryLetter, verbose_name='صاحبان نامه ها')
    IncomingLetterNumber = models.CharField(max_length=20, verbose_name='شماره نامه')
    subject = models.CharField(max_length=50, verbose_name='عنوان نامه')
    document = models.FileField(upload_to='incoming_letters/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('pdfیا jpgتصویرنامه')
)
    
    def __str__(self):
        return self.subject

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
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('تصویرنامه')
,blank=True)
    OutgoingDraft = models.FileField(upload_to='outgoing_letters/draft',
    validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'], message='پسوندهای مجاز doc و docx می باشد')], verbose_name=('فایل ورد نامه')
)
    
    def __str__(self):
        return self.subject

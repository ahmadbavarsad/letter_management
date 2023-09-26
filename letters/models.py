from django.db import models
from django_jalali.db import models as jmodels
from jalali_date.fields import JalaliDateField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


#نامه وارده
class IncomingLetter(models.Model):
    subject = models.CharField(max_length=100,verbose_name=_('عنوان نامه'))
    document = models.FileField(upload_to='incoming_letters/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('تصویرنامه')
)
    IncomingDraft = models.FileField(upload_to='incoming_letters/draft',
    validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'], message='پسوندهای مجاز doc و docx می باشد')], verbose_name=('فایل ورد نامه')
)
    def __str__(self):
        return self.subject


#نامه صادره
class OutgoingLetter(models.Model):
    subject = models.CharField(max_length=100,verbose_name=_('عنوان نامه'))
    document = models.FileField(upload_to='outgoing_letters/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('تصویرنامه')
)
    OutgoingDraft = models.FileField(upload_to='outgoing_letters/draft',
    validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'], message='پسوندهای مجاز doc و docx می باشد')], verbose_name=('فایل ورد نامه')
)
    def __str__(self):
        return self.subject

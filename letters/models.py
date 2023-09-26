from django.db import models
from django_jalali.db import models as jmodels
from jalali_date.fields import JalaliDateField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify


#نامه وارده
class IncomingLetter(models.Model):
    subject = models.CharField(max_length=100,verbose_name=_('عنوان نامه'))
    slug = models.SlugField(unique=True, editable=False)
    document = models.FileField(upload_to='incoming_letters/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('تصویرنامه')
)
    def save(self, *args, **kwargs):
        # Automatically generate the slug from the subject field
        self.slug = slugify(self.subject)
        super(IncomingLetter, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject


#نامه صادره
class OutgoingLetter(models.Model):
    subject = models.CharField(max_length=100,verbose_name=_('عنوان نامه'))

    document = models.FileField(upload_to='outgoing_letters/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg','jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name=('تصویرنامه')
)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the subject field
        self.slug = slugify(self.subject)
        super(OutgoingLetter, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject

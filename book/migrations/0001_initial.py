# Generated by Django 5.0 on 2023-12-09 10:49

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WriterName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'مرد'), ('F', 'زن')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BookName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('BookFile', models.FileField(blank=True, upload_to='outgoing_letters/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg'], message='پسوندهای مجاز pdf و jpg می باشد')], verbose_name='تصویرنامه (pdf یا jpg)')),
                ('OutgoingDraft', models.FileField(upload_to='outgoing_letters/draft', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx'], message='پسوندهای مجاز doc و docx می باشد')], verbose_name='فایل ورد نامه (doc یا docx)')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookcategory')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.auther')),
            ],
        ),
    ]
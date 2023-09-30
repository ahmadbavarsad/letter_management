# Generated by Django 4.2.5 on 2023-09-30 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0011_remove_incomingletter_incomingdraft_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomingletter',
            old_name='LetterNumber',
            new_name='IncomingLetterNumber',
        ),
        migrations.AddField(
            model_name='outgoingletter',
            name='OutgoingLetterNumber',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, verbose_name='شماره نامه'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incomingcategoryletter',
            name='SahebanName',
            field=models.CharField(max_length=100, unique=True, verbose_name='صاحبان نامه ها'),
        ),
        migrations.AlterField(
            model_name='incomingletter',
            name='subject',
            field=models.CharField(max_length=50, verbose_name='عنوان نامه'),
        ),
        migrations.AlterField(
            model_name='outgoingcategoryletter',
            name='SahebanName',
            field=models.CharField(max_length=100, unique=True, verbose_name='صاحبان نامه ها'),
        ),
        migrations.AlterField(
            model_name='outgoingletter',
            name='subject',
            field=models.CharField(max_length=50, verbose_name='عنوان نامه'),
        ),
    ]
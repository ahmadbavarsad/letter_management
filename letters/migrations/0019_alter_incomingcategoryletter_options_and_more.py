# Generated by Django 4.1 on 2023-11-27 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0018_alter_incomingletter_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomingcategoryletter',
            options={'verbose_name': 'صاحبان نامه', 'verbose_name_plural': 'صاحبان نامه'},
        ),
        migrations.RemoveField(
            model_name='incomingletter',
            name='slug',
        ),
        migrations.AlterModelTable(
            name='incomingcategoryletter',
            table='IncomingCategoryLetter',
        ),
    ]

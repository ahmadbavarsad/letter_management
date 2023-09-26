# Generated by Django 4.2.5 on 2023-09-26 06:50

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_alter_outgoingletter_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingletter',
            name='received_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='نامه های رسیده'),
        ),
        migrations.AlterField(
            model_name='outgoingletter',
            name='sent_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='نامه های ارسالی'),
        ),
    ]

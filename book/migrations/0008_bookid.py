# Generated by Django 5.0 on 2023-12-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_bookname_options_alter_bookname_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdNumber', models.CharField(max_length=10, verbose_name='کد کتاب')),
            ],
            options={
                'verbose_name': 'کد کتاب',
                'verbose_name_plural': 'کد کتاب ها',
                'db_table': 'id_Number',
            },
        ),
    ]

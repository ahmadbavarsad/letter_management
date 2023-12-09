# Generated by Django 5.0 on 2023-12-09 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_bookcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublisherName', models.CharField(max_length=64, verbose_name='انتشارات')),
            ],
            options={
                'verbose_name': 'انتشاراتی',
                'verbose_name_plural': 'انتشاراتی',
                'db_table': 'publisher_category',
            },
        ),
        migrations.AlterField(
            model_name='bookname',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookcategory', verbose_name='دسته بندی موضوعی'),
        ),
        migrations.AddField(
            model_name='bookname',
            name='publisher',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='book.publishercategory', verbose_name='انتشارات'),
            preserve_default=False,
        ),
    ]

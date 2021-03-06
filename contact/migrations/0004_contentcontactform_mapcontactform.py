# Generated by Django 3.2.5 on 2021-08-31 03:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210827_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentcontactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Nội dung liên hệ')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Nội dung liên hệ',
            },
        ),
        migrations.CreateModel(
            name='MapcontactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Bản đồ')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bản đồ liên hệ',
            },
        ),
    ]

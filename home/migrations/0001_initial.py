# Generated by Django 3.2.5 on 2021-08-27 03:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homeForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Nội dung Trang chủ',
            },
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-31 04:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NhomDichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nhóm dịch vụ')),
            ],
            options={
                'verbose_name_plural': 'Dịch vụ',
            },
        ),
        migrations.CreateModel(
            name='DichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(max_length=500, verbose_name='Tên dịch vụ')),
                ('tomtat', models.CharField(max_length=1000, verbose_name='Tóm tắt')),
                ('noidung', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Nội dung')),
                ('hinh', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Hình')),
                ('ngaynhap', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ngày nhập')),
                ('nhomdichvu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dichvu.nhomdichvu')),
            ],
            options={
                'verbose_name_plural': 'Chi tiết dịch vụ',
            },
        ),
    ]
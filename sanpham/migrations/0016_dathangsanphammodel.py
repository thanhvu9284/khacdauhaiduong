# Generated by Django 3.2.5 on 2021-10-01 07:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0015_auto_20210917_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='DathangSanPhamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=150, verbose_name='Tên người liên hệ')),
                ('dienthoai', models.CharField(max_length=50, verbose_name='Điện thoại')),
                ('diachi', models.CharField(max_length=500, verbose_name='Địa chỉ')),
                ('soluong', models.CharField(max_length=50, verbose_name='Số lượng')),
                ('noidung', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Thông tin đặt hàng',
            },
        ),
    ]

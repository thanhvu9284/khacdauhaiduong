# Generated by Django 3.2.5 on 2021-10-01 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0027_auto_20211001_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dathangsanphammodel',
            name='sanpham',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanpham.sanpham'),
        ),
    ]
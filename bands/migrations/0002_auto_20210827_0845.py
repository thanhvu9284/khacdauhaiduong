# Generated by Django 3.2.5 on 2021-08-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='band',
            options={'verbose_name_plural': 'Ban nhạc'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name_plural': 'Thành viên Ban nhạc'},
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Tên ban nhạc'),
        ),
        migrations.AlterField(
            model_name='member',
            name='instrument',
            field=models.CharField(choices=[('g', 'Đàn Guitar'), ('b', 'Bass'), ('d', 'Trống')], max_length=1, verbose_name='Công cụ'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Tên thành viên'),
        ),
    ]

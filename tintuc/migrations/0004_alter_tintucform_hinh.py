# Generated by Django 3.2.5 on 2021-10-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tintuc', '0003_alter_tintucform_tomtat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintucform',
            name='hinh',
            field=models.ImageField(blank=True, null=True, upload_to='tintuc/', verbose_name='Hình'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-31 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contentcontactform_mapcontactform'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name_plural': 'Thông tin người liên hệ'},
        ),
        migrations.AlterField(
            model_name='contactform',
            name='username',
            field=models.CharField(max_length=25, verbose_name='Tên người liên hệ'),
        ),
    ]
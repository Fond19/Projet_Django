# Generated by Django 2.1.1 on 2018-09-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180911_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

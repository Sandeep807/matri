# Generated by Django 3.2.8 on 2021-10-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211021_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='registration',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

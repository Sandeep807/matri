# Generated by Django 3.2.8 on 2021-10-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_booking_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverregistration',
            name='type',
            field=models.CharField(default='Driver', max_length=100),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-21 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='driver',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='taxi.driverregistration'),
            preserve_default=False,
        ),
    ]

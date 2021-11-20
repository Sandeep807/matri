# Generated by Django 3.2.8 on 2021-11-20 09:58

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211120_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='employed_in',
            field=models.CharField(blank=True, choices=[('Government/PSU', 'Government/PSU'), ('Private', 'Private'), ('Business', 'Business'), ('Defence', 'Defence'), ('Self Employed', 'Self Employed'), ('Not Working', 'Not Working')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='profile_created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
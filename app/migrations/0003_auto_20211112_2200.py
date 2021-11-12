# Generated by Django 3.2.8 on 2021-11-12 16:30

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_registration_caste'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='peta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
    ]
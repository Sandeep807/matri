# Generated by Django 3.2.8 on 2021-11-20 10:01

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211120_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
    ]

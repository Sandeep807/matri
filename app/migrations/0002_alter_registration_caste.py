# Generated by Django 3.2.8 on 2021-11-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='caste',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
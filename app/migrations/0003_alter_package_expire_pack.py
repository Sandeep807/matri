# Generated by Django 3.2.8 on 2021-10-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211028_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='expire_pack',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

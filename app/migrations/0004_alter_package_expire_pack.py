# Generated by Django 3.2.8 on 2021-10-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_package_expire_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='expire_pack',
            field=models.DateField(blank=True, null=True),
        ),
    ]

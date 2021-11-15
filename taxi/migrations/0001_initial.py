# Generated by Django 3.2.8 on 2021-11-15 18:42

import app.managers
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('child_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('source_address', models.TextField()),
                ('destination_address', models.TextField()),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('booking_time', models.TimeField()),
                ('type_vehicle', models.CharField(choices=[('Select Options', 'Select Options'), ('TOYOTA ETIOS', 'TOYOTA ETIOS'), ('SWIFT DZIRE', 'SWIFT DZIRE'), ('MAHINDRA VERITO', 'MAHINDRA VERITO'), ('INNOVA 6+1', 'INNOVA 6+1'), ('INNOVA 7+1', 'INNOVA 7+1'), ('TEMPO TRAVELLER', 'TEMPO TRAVELLER'), ('MINI BUS', 'MINI BUS'), ('SEDAN', 'SEDAN'), ('HATCHBACK', 'HATCHBACK')], max_length=100)),
                ('amount', models.FloatField(default=500)),
                ('is_cancel', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverRegistration',
            fields=[
                ('registration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.registration')),
                ('licence', models.CharField(max_length=20)),
                ('aadhar_card', models.IntegerField()),
                ('pan_card', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='driver')),
                ('type', models.CharField(default='Driver', max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.registration',),
            managers=[
                ('objects', app.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('oder_id', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.booking')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='taxi.driverregistration'),
        ),
    ]

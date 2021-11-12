# Generated by Django 3.2.8 on 2021-11-12 16:53

import app.managers
import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('profile_created_by', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Myelf', 'Myself'), ('Son', 'Son'), ('Sister', 'Sister'), ('Brother', 'Brother'), ('Relative', 'Relative'), ('Friend', 'Friend')], max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Hindu', 'Hindu'), ('Muslim-All', 'Muslim-All'), ('Muslim-Shia', 'Muslim-Shia'), ('Muslim-Sunni', 'Muslim-Sunni'), ('Muslim-Others', 'Muslim-Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain-All', 'Jain-All'), ('Jain-Digambar', 'Jain-Digambar'), ('Jain-Shwetambar', 'Jain-Shwetambar'), ('Jain-Others', 'Jain-Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Jewish', 'Jewish'), ('Inter-Religion', 'Inter-Religion')], max_length=200, null=True)),
                ('mother_tongue', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Malayalam', 'Malayalam'), ('Marathi', 'Marathi'), ('Marwari', 'Marwari'), ('Oriya', 'Oriya'), ('Punjabi', 'Punjabi'), ('Sindhi', 'Sindhi'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Urdu', 'Urdu'), ('Angika', 'Angika'), ('Arunachali', 'Arunachali'), ('Assamese', 'Assamese'), ('Awadhi', 'Awadhi'), ('Bhojpuri', 'Bhojpuri'), ('Brij', 'Brij'), ('Bihari', 'Bihari'), ('Badaga', 'Badaga'), ('Chatisgarhi', 'Chatisgarhi'), ('Dogri', 'Dogri'), ('English', 'English'), ('French', 'French'), ('Garhwali', 'Garhwali'), ('Garo', 'Garo'), ('Haryanvi', 'Haryanvi'), ('Himachali/Pahari', 'Himachali/Pahari'), ('Kanauji', 'Kanauji'), ('Kashmiri', 'Kashmiri'), ('Khandesi', 'Khandesi'), ('Khasi', 'Khasi'), ('Konkani', 'Konkani'), ('Koshali', 'Koshali'), ('Kumaoni', 'Kumaoni'), ('Kutchi', 'Kutchi'), ('Lepcha', 'Lepcha'), ('Ladacki', 'Ladacki'), ('Magahi', 'Magahi'), ('Maithili', 'Maithili'), ('Manipuri', 'Manipuri'), ('Miji', 'Miji'), ('Mizo', 'Mizo'), ('Monpa', 'Monpa'), ('Nicobarese', 'Nicobarese'), ('Nepali', 'Nepali'), ('Rajasthani', 'Rajasthani'), ('Sanskrit', 'Sanskrit'), ('Santhali', 'Santhali'), ('Sourashtra', 'Sourashtra'), ('Tripuri', 'Tripuri'), ('Tulu', 'Tulu'), ('Bagri Rajasthani', 'Bagri Rajasthani'), ('Dhundhari/Jaipuri', 'Dhundhari/Jaipuri'), ('Gujari/Gojari', 'Gujari/Gojari'), ('Harauti', 'Harauti'), ('Lambadi', 'Lambadi'), ('Malvi', 'Malvi'), ('Mewari', 'Mewari'), ('Mewati/Ahirwati', 'Mewati/Ahirwati'), ('Nimadi', 'Nimadi'), ('Shekhawati', 'Shekhawati'), ('Wagdi', 'Wagdi')], max_length=100, null=True)),
                ('caste', models.CharField(blank=True, max_length=1000, null=True)),
                ('gotra', models.CharField(blank=True, max_length=100, null=True)),
                ('peta', models.CharField(blank=True, max_length=100, null=True)),
                ('dosh', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('', 'Do not Know')], max_length=100, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Never Married', 'Never Married'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced'), ('Awaiting Divorce', 'Awaiting Divorce')], max_length=100, null=True)),
                ('any_disability', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('None', 'None'), ('Physically Challenged', 'Physically Challenged')], max_length=100, null=True)),
                ('family_status', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Middle Class', 'Middle Class'), ('Affluent', 'Affluent'), ('Upper Middle Class', 'Upper Middle Class'), ('Rich', 'Rich')], max_length=100, null=True)),
                ('family_type', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Joint', 'Joint'), ('Nuclear', 'Nuclear')], max_length=100, null=True)),
                ('family_value', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Orthodox', 'Orthodox'), ('Traditional', 'Traditional'), ('Moderate', 'Moderate'), ('Liberal', 'Liberal')], max_length=100, null=True)),
                ('education', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Aeronautical Engineering', 'Aeronautical Engineering'), ('B.Arch', 'B.Arch'), ('BCA', 'BCA'), ('B.E', 'B.E'), ('B.Plan', 'B.Plan'), ('B.Sc IT/Computer Science', 'B.Sc IT/Computer Science'), ('B.Tech', 'B.Tech'), ('Other Bacherlor Degree in Engineering/Computers', 'Other Bacherlor Degree in Engineering/Computers'), ('B.S(Engineering)', 'B.S(Engineering)'), ('M.Arch', 'M.Arch'), ('MCA', 'MCA'), ('ME', 'ME'), ('M.Sc IT/Computer Science', 'M.Sc IT/Computer Science'), ('M.S(Engg)', 'M.S(Engg)'), ('M.Tech', 'M.Tech'), ('PGDCA', 'PGDCA'), ('Other Master Degree in Engineering/Computer', 'Other Master Degree in Engineering/Computer'), ('B.A', 'B.A'), ('B.Com', 'B.Com'), ('B.Ed', 'B.Ed'), ('BFA', 'BFA'), ('BFT', 'BFT'), ('BLIS', 'BLIS'), ('B.M.M', 'B.M.M'), ('B.Sc', 'B.Sc'), ('B.S.W', 'B.S.W'), ('B.Phil', 'B.Phil'), ('M.A', 'M.A'), ('M.Sc', 'M.Sc'), ('BBA', 'BBA'), ('MBA', 'MBA'), ('Software Engineer', 'Software Engineer')], max_length=1000, null=True)),
                ('employed_in', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Government/PSU', 'Government/PSU'), ('Private', 'Private'), ('Business', 'Business'), ('Defence', 'Defence'), ('Self Employed', 'Self Employed'), ('Not Working', 'Not Working')], max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Software Professional', 'Software Professional'), ('Teaching', 'Teaching'), ('Executive', 'Executive'), ('Doctor', 'Doctor'), ('Manager', 'Manager'), ('Professor/Lecturer', 'Professor/Lecturer'), ('Officer', 'Officer'), ('Human Resources Professional', 'Human Resources Professional'), ('Pilot', 'Pilot'), ('Air Hostess', 'Air Hostess'), ('Chartered Accountant', 'Chartered Accountant'), ('Fashion Designer', 'Fashion Designer'), ('MakeUp Artist', 'MakeUp Artist'), ('Civil Services(IAS/IPS/IRS)', 'Civil Services(IAS/IPS/IRS)')], max_length=100, null=True)),
                ('annual_income', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('0-1Lakhs', '0-1Lakhs'), ('1-2lakhs', '1-2lakhs'), ('2-3lakhs', '2-3lakhs'), ('3-4lakhs', '3-4lakhs'), ('4-5lakhs', '4-5lakhs'), ('5-6lakhs', '5-6lakhs'), ('6-7lakhs', '6-7lakhs'), ('7-8lakhs', '7-8lakhs'), ('8-9lakhs', '8-9lakhs'), ('9-10lakhs', '9-10lakhs'), ('10-12lakhs', '10-12lakhs'), ('12-14lakhs', '12-14lakhs'), ('14-16lakhs', '14-16lakhs'), ('16-18lakhs', '16-18lakhs'), ('18-20lakhs', '18-20lakhs'), ('20-25lakhs', '20-25kakhs'), ('25-30lakhs', '25-30lakhs'), ('30-35lakhs', '30-35lakhs'), ('35-40lakhs', '35-40lakhs'), ('40-45lakhs', '40-45lakhs'), ('45-50lakhs', '45-50lakhs'), ('50-60lakhs', '50-60lakhs'), ('60-70lakhs', '60-70lakhs'), ('70-80lakhs', '70-80lakhs'), ('80-90lakhs', '80-90lakhs'), ('90-1crore', '90-1crore'), ('1crore & Above', '1crore & Above')], max_length=1000, null=True)),
                ('work_location', models.CharField(blank=True, choices=[('Select Options', 'Select Options'), ('Indian', 'Indian')], max_length=100, null=True)),
                ('residing_state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='matri/image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', app.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.IntegerField(default=app.models.generate_id, editable=False, primary_key=True, serialize=False)),
                ('subscription_amount', models.IntegerField()),
                ('membership', models.CharField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')], max_length=100)),
                ('expire_pack', models.DateField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('registeruser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.IntegerField(default=app.models.generate_id, primary_key=True, serialize=False)),
                ('tranc_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=100, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='app.package')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

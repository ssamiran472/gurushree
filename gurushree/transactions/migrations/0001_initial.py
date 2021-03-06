# Generated by Django 2.2.12 on 2020-07-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_type', models.CharField(max_length=32, null=True)),
                ('title', models.CharField(max_length=32, null=True)),
                ('gender', models.CharField(max_length=32, null=True)),
                ('p_name', models.CharField(max_length=32, null=True)),
                ('year', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('day', models.IntegerField(null=True)),
                ('mobile_number', models.CharField(max_length=32, null=True)),
                ('address', models.CharField(max_length=32, null=True)),
                ('email_id', models.CharField(max_length=32, null=True)),
                ('address2', models.CharField(max_length=32, null=True)),
                ('location', models.CharField(max_length=32, null=True)),
                ('pincode', models.CharField(max_length=32, null=True)),
                ('alternateContact', models.CharField(max_length=32, null=True)),
                ('marital', models.CharField(max_length=32, null=True)),
                ('occupation', models.CharField(max_length=32, null=True)),
                ('religion', models.CharField(max_length=32, null=True)),
                ('father_name', models.CharField(max_length=32, null=True)),
                ('blood_group', models.CharField(max_length=32, null=True)),
                ('nationality', models.CharField(max_length=32, null=True)),
                ('id_type', models.CharField(max_length=32, null=True)),
                ('id_number', models.CharField(max_length=32, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('AddedBY', models.CharField(max_length=32, null=True)),
                ('Addeddate', models.DateTimeField(auto_now_add=True)),
                ('editedby', models.CharField(max_length=32, null=True)),
                ('editeddate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

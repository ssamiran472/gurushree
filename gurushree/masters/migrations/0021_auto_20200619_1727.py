# Generated by Django 2.2.12 on 2020-06-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0020_generaltype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountype',
            name='password',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='discountype',
            name='userId',
            field=models.CharField(max_length=32),
        ),
    ]
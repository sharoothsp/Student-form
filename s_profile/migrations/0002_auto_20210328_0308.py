# Generated by Django 2.2.2 on 2021-03-27 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprofile',
            name='Phone_number',
            field=models.IntegerField(null=True),
        ),
    ]

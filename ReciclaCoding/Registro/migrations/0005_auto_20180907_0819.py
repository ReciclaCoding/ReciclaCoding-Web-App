# Generated by Django 2.1.1 on 2018-09-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_auto_20180907_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

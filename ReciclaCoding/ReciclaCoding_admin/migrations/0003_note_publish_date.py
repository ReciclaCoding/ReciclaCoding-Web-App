# Generated by Django 2.1.1 on 2018-09-05 23:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ReciclaCoding_admin', '0002_auto_20180905_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

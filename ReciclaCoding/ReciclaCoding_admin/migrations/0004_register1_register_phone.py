# Generated by Django 2.1.1 on 2018-09-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReciclaCoding_admin', '0003_note_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='register1',
            name='register_phone',
            field=models.CharField(default=123456789, max_length=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_sitter_description_alter_booking_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='city',
            field=models.CharField(default='New York', max_length=255),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-13 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_booking_sitter_alter_pet_primary_care_sitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='primary_care_sitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_pets', to='api.sitter'),
        ),
    ]
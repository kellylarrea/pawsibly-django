# Generated by Django 4.0.1 on 2022-01-13 05:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_review_pet_owner_review_sitter_sitter_sitter_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='sitter_reviews',
            field=models.ManyToManyField(through='api.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]

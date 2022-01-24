from django.db import models
from django.db.models.fields import related 
from django.contrib.auth import get_user_model
from .sitter import Sitter



class Pet(models.Model):
    name = models.CharField(null=True, max_length=100)
    pet_owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name="pets_owned"
    )

    def __str__(self):
        return self.name


    def as_dict(self):
        return {
            'name': self.name
    }
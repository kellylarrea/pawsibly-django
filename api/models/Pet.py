from django.db import models
from django.db.models.fields import related 
from django.contrib.auth import get_user_model
from .sitter import Sitter

def upload_path(instance, filename):
    return '/'.join(['pets', str(instance.name), filename])

class Pet(models.Model):

    name = models.CharField(null =True,max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='images/')
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
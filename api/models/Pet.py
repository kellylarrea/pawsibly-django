from django.db import models
from django.db.models.fields import related 
from django.contrib.auth import get_user_model
from .booking import Booking
from .user import User


class Pet(models.Model):
    name = models.CharField(null =True,max_length=100)
    pet_owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name="pet_owned"
    )
    pet_sitter = models.ForeignKey(User, related_name='client_pet', on_delete=models.CASCADE,blank=True, null=True)
    # booking_pet = models.ManyToManyField(
    # User,
    # through=Booking,
    # through_fields=('owner_pet','sitter')
    # )

   

    def __str__(self):
        return self.name


    def as_dict(self):
        return {
            'name': self.name
    }
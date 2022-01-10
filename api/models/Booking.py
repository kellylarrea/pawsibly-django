from django.db import models
from django.contrib.auth import get_user_model
# from .user import User
# from .pet import Pet


# Create your models here.
class Booking(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  owner_pet = models.ForeignKey("Pet", on_delete=models.CASCADE)
  sitter = models.ForeignKey("User", on_delete=models.CASCADE)
  
  

  def __str__(self):
    return f'{self.id}'

  def as_dict(self):
    return {
        'start_date': self.start_date,
        'end_data': self.end_date,
        'sitter': self.sitter,
      }
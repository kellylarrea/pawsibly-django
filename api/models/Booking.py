from django.db import models
from django.contrib.auth import get_user_model
from pet import Pet

# Create your models here.
class Booking(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  pet = models.ForeignKey(
      Pet,
      on_delete=models.CASCADE
  )
  sitter = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return self.start_date

  def as_dict(self):
    return {
        'start_date': self.start_data,
        'end_data': self.end_data,
      }

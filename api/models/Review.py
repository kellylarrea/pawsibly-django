from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Review(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  review = models.CharField(max_length=500)
  rating = models.IntegerField(max_length=5)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  sitter = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  pet_owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    #return f"The mango named '{self.name}' is {self.color} in color. It is {self.ripe} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Review models"""
    return {
        'review': self.review,
        'rating': self.rating,
    }

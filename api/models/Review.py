from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from ..models.sitter import Sitter
class Review(models.Model):
  # define fields

  review = models.CharField(max_length=500)
  rating = models.DecimalField(max_digits=7, decimal_places=2)
  sitter = models.ForeignKey(Sitter,on_delete=models.CASCADE,null=True)
  pet_owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)



  def __str__(self):
      return self.review
      

  def as_dict(self):
    """Returns dictionary version of Review models"""
    return {
        'review': self.review,
        'rating': self.rating,
        
    }


from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Review(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  review = models.CharField(max_length=500)
  rating = models.IntegerField(null=True, default=0, validators=[MaxValueValidator(5)])
  sitter = models.ForeignKey('Sitter',on_delete=models.CASCADE,null=True,blank=True)
  pet_owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)


  def __str__(self):
      return self.review
      
  def as_dict(self):
    """Returns dictionary version of Review models"""
    return {
        'review': self.review,
        'rating': self.rating,
        
    }

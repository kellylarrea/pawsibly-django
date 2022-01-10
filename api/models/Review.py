from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Review(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  review = models.CharField(max_length=500)
  rating = models.IntegerField(null=True, default=0, validators=[MaxValueValidator(5)])
  created_at = models.DateTimeField(auto_now_add=True)
  sitter = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  pet_owner = models.ForeignKey(
      get_user_model(), related_name="client_reviews",
      on_delete=models.CASCADE
  )

  def __str__(self):
      return self.review
      
  def as_dict(self):
    """Returns dictionary version of Review models"""
    return {
        'id':self.id,
        'review': self.review,
        'rating': self.rating,
        'created_at': self.created_at
    }

from django.contrib.auth import get_user_model
from django.db import models



class Sitter(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    first_name = models.CharField(max_length=255, default='Jane')
    last_name = models.CharField(max_length=255, default='Doe')
    zipcode = models.CharField(max_length = 5, default='12345')
    supersitter = models.BooleanField(null=True, blank=True)
    pricing = models.IntegerField(null=True)
    numReviews = models.IntegerField(default=0) 
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0)
   
   

    
 

    def __str__(self):
        return self.first_name
      
    def as_dict(self):
        return {
            'rating': self.rating,
            'first_name': self.first_name,

    }
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import related




# Create your models here.
class Booking(models.Model):
  start_date = models.DateTimeField()  
  end_date = models.DateTimeField()
  pet = models.ForeignKey('Pet',on_delete=models.CASCADE, blank=True,null=True)
  sitter = models.ForeignKey('Sitter', on_delete=models.CASCADE)
 
  

  def __str__(self):
    return f'{self.id}'

  def as_dict(self):
    return {
        'start_date': self.start_date,
        'end_data': self.end_date,
       
      }

    # I think I helped with first issue right? /sttiter url error
    # we have spent 15mins - $30
    # 
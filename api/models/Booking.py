from django.contrib.auth import get_user, get_user_model
from django.db import models 
from django.db.models.fields import related
from .sitter import Sitter





# Create your models here.
class Booking(models.Model):
  start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
  end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
  pet_owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True, blank=True)
  sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE,null=True, blank=True)
 

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
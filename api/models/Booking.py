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
<<<<<<< HEAD
  owner_pet = models.ForeignKey("Pet", on_delete=models.CASCADE)
  sitter = models.ForeignKey("User", on_delete=models.CASCADE)
  
=======
  # owner_pet = models.ForeignKey("Pet", related_name = "pet_booking", on_delete=models.CASCADE)
  owner_of_pet = models.ForeignKey(
      get_user_model(), related_name = "pets_owmed",
      on_delete=models.CASCADE, blank=True,null=True
  )
  sitter = models.ForeignKey("User",related_name="sitter_bookings", on_delete=models.CASCADE)
 
>>>>>>> refs/remotes/origin/main
  

  def __str__(self):
    return f'{self.id}'

  def as_dict(self):
    return {
        'start_date': self.start_date,
        'end_data': self.end_date,
<<<<<<< HEAD
        'sitter': self.sitter,
      }
=======
        'sitter': self.sitter
      }
>>>>>>> refs/remotes/origin/main

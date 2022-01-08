from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.pet_views import Pet, PetDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('pets', Pet.as_view(), name='pets'),
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('pets/', Pet.as_view(), name='pets'),
    path('pets/<int:pk>/', PetDetail.as_view(), name='pet_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]

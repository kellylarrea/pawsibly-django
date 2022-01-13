from django.urls import path
from .views.mango_views import Mangos, MangoDetail

from .views.pet_views import Pets, PetDetail
from .views.sitter_views import Sitters, SitterDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword,  Profile
from .views.booking_views import Bookings, BookingsDetail
from .views.review_views import Reviews, ReviewsDetail


# from views.booking_views import Review


urlpatterns = [
  	# Restful routing
    path('profile',Profile.as_view(), name='users'),
    # path('users',Sitters.as_view(), name='users'),
    path('sitters',Sitters.as_view(), name='users'),
    path('users/<int:pk>/',PetDetail.as_view(), name='pet_detail'),
    path('users/<int:pk>/',SitterDetail.as_view(), name='sitter_detail'),
    path('bookings',Bookings.as_view(), name='bookings'),
    path('bookings/<int:pk>/', BookingsDetail.as_view(), name='bookings_detail'),
    path('pets', Pets.as_view(), name='pets'),
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('pets/', Pets.as_view(), name='pets'),
    path('pets/<int:pk>', PetDetail.as_view(), name='pet_detail'),
    path('reviews/', Reviews.as_view(), name='reviews'),
    path('reviews/<int:pk>', ReviewsDetail.as_view(), name='reviews_detail'),
    path('sign-up', SignUp.as_view(), name='sign-up'),
    path('sign-in', SignIn.as_view(), name='sign-in'),
    path('sign-out', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]

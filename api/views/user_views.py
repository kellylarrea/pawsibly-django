

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from ..models.user import User
from ..serializers import  UserSerializer, UserRegisterSerializer,  ChangePasswordSerializer, UserReadSerializer

class Sitters(generics.ListCreateAPIView):
    # permission_classes=(IsAuthenticated,) 
    # serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserReadSerializer
    def get(self, request):
        """Index request"""
        print(request)
        # Get all the pets:
        # pets = Pet.objects.all()
        # Filter the pets by owner, so you can only see your owned pets
        user = User.objects.filter(sitter = False)
        # Run the data through the serializer
        data = UserReadSerializer(user, many=True).data
        return Response({ 'user': data }
        )

class SitterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=()
    serializer_class = UserReadSerializer
    def get(self, request, pk):
        """Show request"""
        # Locate the booking to show
        user = get_object_or_404(User, pk=pk)

        # Run the data through the serializer so it's formatted
        data = UserReadSerializer(user).data
        return Response({ 'user': data })


    # def post(self, request):
    #     """Create request"""
    #     # Add user to request data object
    #     request.data['pet']['owner'] = request.user.id
    #     # Serialize/create pet
    #     pet = PetSerializer(data=request.data['pet'])
    #     # If the pet data is valid according to our serializer...
    #     if pet.is_valid():
    #         # Save the created pet & send a response
    #         pet.save()
    #         return Response({ 'pet': pet.data }, status=status.HTTP_201_CREATED)
    #     # If the data is not valid, return a response with the errors
    #     return Response(pet.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class SignUp(generics.CreateAPIView):
    # Override the authentication/permissions classes so this endpoint
    # is not authenticated & we don't need any permissions to access it.
    authentication_classes = ()
    permission_classes = ()

    # Serializer classes are required for endpoints that create data
    serializer_class = UserRegisterSerializer

    def post(self, request):
        # Pass the request data to the serializer to validate it
        user = UserRegisterSerializer(data=request.data)
        # If that data is in the correct format...
        if user.is_valid():
            # Actually create the user using the UserSerializer (the `create` method defined there)
            created_user = UserSerializer(data=user.data)

            if created_user.is_valid():
                # Save the user and send back a response!
                created_user.save()
                return Response({ 'user': created_user.data }, status=status.HTTP_201_CREATED)
            else:
                return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(generics.CreateAPIView):
    # Override the authentication/permissions classes so this endpoint
    # is not authenticated & we don't need any permissions to access it.
    authentication_classes = ()
    permission_classes = ()

    # Serializer classes are required for endpoints that create data
    serializer_class = UserSerializer

    def post(self, request):
        creds = request.data
        print(creds)
        # We can pass our  and password along with the request to the
        # `authenticate` method. If we had used the default user, we would need
        # to send the `username` instead of `email`.
        user = authenticate(request, email=creds['credentials']['email'], password=creds['credentials']['password'])
        # Is our user is successfully authenticated...
        if user is not None:
            # And they're active...
            if user.is_active:
                # Log them in!
                login(request, user)
                # Finally, return a response with the user's token
                return Response({
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'token': user.get_auth_token()
                    }
                })
            else:
                return Response({ 'msg': 'The account is inactive.' }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SignOut(generics.DestroyAPIView):
    def delete(self, request):
        # Remove this token from the user
        request.user.delete_token()
        # Logout will remove all session data
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePassword(generics.UpdateAPIView):
    def partial_update(self, request):
        user = request.user
        # Pass data through serializer
        serializer = ChangePasswordSerializer(data=request.data['passwords'])
        if serializer.is_valid():
            # This is included with the Django base user model
            # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User.check_password
            if not user.check_password(serializer.data['old']):
                return Response({ 'msg': 'Wrong password' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # set_password will also hash the password
            # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
            user.set_password(serializer.data['new'])
            user.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
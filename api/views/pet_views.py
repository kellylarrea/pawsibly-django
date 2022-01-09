from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.pet import Pet
from ..serializers import PetSerializer

# Create your views here.
class Pets(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PetSerializer

    def get(self, request):
        """Index request"""
        # Get all the pets:
        # pets = Pet.objects.all()
        # Filter the pets by owner, so you can only see your owned pets
        pets = Pet.objects.filter(pet_owner=request.user.id)
        # Run the data through the serializer
        data = PetSerializer(pets, many=True).data
        return Response({ 'pets': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['pet']['owner'] = request.user.id
        # Serialize/create pet
        pet = PetSerializer(data=request.data['pet'])
        # If the pet data is valid according to our serializer...
        if pet.is_valid():
            # Save the created pet & send a response
            pet.save()
            return Response({ 'pet': pet.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(pet.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetSerializer
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the pet to show
        pet = get_object_or_404(Pet, pk=pk)
        # Only want to show owned pets?
        if request.user != pet.pet_owner:
            raise PermissionDenied('Unauthorized, you do not own this Pet')

        # Run the data through the serializer so it's formatted
        data = PetSerializer(pet).data
        return Response({ 'pet': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate pet to delete
        mango = get_object_or_404(Mango, pk=pk)
        # Check the pet's owner against the user making this request
        if request.user != pet.owner:
            raise PermissionDenied('Unauthorized, you do not own this pet')
        # Only delete if the user owns the  mango
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Pet
        # get_object_or_404 returns a object representation of our Pet
        pet = get_object_or_404(Pet, pk=pk)
        # Check the pets's owner against the user making this request
        if request.user != pet.owner:
            raise PermissionDenied('Unauthorized, you do not own this pet')

        # Ensure the owner field is set to the current user's ID
        request.data['pet']['owner'] = request.user.id
        # Validate updates with serializer
        data = PetSerializer(pet, data=request.data['pet'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

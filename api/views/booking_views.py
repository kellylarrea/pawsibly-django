from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.booking import booking
from ..serializers import BookingSerializer

# Create your views here.
class Booking(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = BookingSerializer
    def get(self, request):
        """Index request"""
        # Get all the bookings:
        # bookings = Booking.objects.all()
        # Filter the bookings by owner, so you can only see the user's bookings
        bookings = Booking.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = BookingSerializer(bookings, many=True).data
        return Response({ 'bookings': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['booking']['owner'] = request.user.id
        # Serialize/create booking
        booking = BookingSerializer(data=request.data['booking'])
        # If the booking data is valid according to our serializer...
        if booking.is_valid():
            # Save the created booking & send a response
            booking.save()
            return Response({ 'booking': booking.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(booking.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the booking to show
        booking = get_object_or_404(Booking, pk=pk)
        # Only want to show user's booking?
        if request.user != booking.owner:
            raise PermissionDenied('Unauthorized, you do not own this booking')

        # Run the data through the serializer so it's formatted
        data = BookingSerializer(booking).data
        return Response({ 'booking': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate a booking to delete
        booking = get_object_or_404(Booking, pk=pk)
        # Check the booking's owner against the user making this request
        if request.user != booking.owner:
            raise PermissionDenied('Unauthorized, you do not own this booking')
        # Only delete if the user owns the booking
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Booking
        # get_object_or_404 returns a object representation of our Booking
        pet = get_object_or_404(Pet, pk=pk)
        # Check the pets's owner against the user making this request
        if request.user != booking.owner:
            raise PermissionDenied('Unauthorized, you do not own this booking')

        # Ensure the owner field is set to the current user's ID
        request.data['booking']['owner'] = request.user.id
        # Validate updates with serializer
        data = BookingSerializer(booking, data=request.data['booking'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

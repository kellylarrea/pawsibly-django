from importlib.resources import contents
from math import prod
from pickletools import read_uint1
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from ..models.sitter import Sitter
from ..models.review import Review
from ..serializers import ReviewSerializer
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


class Reviews(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ReviewSerializer

    def get(self, request, pk):
        """Index request"""
        # Get all the reviews:
        # reviews = Review.objects.all()
        # Filter the reviews by owner, so you can only see your owned reviews
        reviews = Review.objects.filter(sitter=pk)
        # Run the data through the serializer
        data = ReviewSerializer(reviews, many=True).data
        return Response({'reviews': data})


    #  def post(self, request, pk):
    #     """Create request"""
    #     print(request.data)
    #     # Add user to request data object
    #     # Serialize/create review
    #     grabsitter = get_object_or_404(Sitter, pk=pk)
    #     review_user = request.user
    #     pet_owner = Review(pet_owner = review_user)
    #     sitter = Review(sitter = grabsitter)
    #     review = ReviewSerializer(pet_owner,sitter, data=request.data,)
    #     # If the review data is valid according to our serializer...
    #     if review.is_valid():
    #         # Save the created review & send a response
    #         r = review.save()
    #         return Response({ 'review': review.data }, status=status.HTTP_201_CREATED)
    #     # # If the data is not valid, return a response with the errors
    #     return Response(review.data, status=status.HTTP_400_BAD_REQUEST)
class ReviewsDetail(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ReviewSerializer
    
    def get(self, request, pk):
        """Index request"""
        # Get all the reviews:
        # reviews = Review.objects.all()
        # Filter the reviews by owner, so you can only see your owned reviews
        reviews = Review.objects.filter(sitter=pk)
        # Run the data through the serializer
        data = ReviewSerializer(reviews, many=True).data
        return Response({'reviews': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate review to delete
        review = get_object_or_404(Review, pk=pk)
        # Check the review's owner against the user making this request
        if request.user != review.owner:
            raise PermissionDenied('Unauthorized, you do not own this review')
        # Only delete if the user owns this review
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Review
        # get_object_or_404 returns a object representation of our Review
        review = get_object_or_404(Review, pk=pk)
        # Check the review's owner against the user making this request
        if request.user != review.pet_owner:
            raise PermissionDenied('Unauthorized, you do not own this review')

        # Ensure the owner field is set to the current user's ID
        # Validate updates with serializer
        data = ReviewSerializer(review,data=request.data['review'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)




   
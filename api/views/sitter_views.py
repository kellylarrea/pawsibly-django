from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from ..models.sitter import Sitter
from ..serializers import SitterSerializer

# Create your views here.
class Sitters(generics.ListCreateAPIView):
    permission_classes=()
    serializer_class = SitterSerializer
    def get(self, request):
        """Index request"""
        # Get all the sitters:
        # sitters = Sitter.objects.all()
        # Filter the sitters by zipcode
        print("get1")
        sitters = Sitter.objects.all()
        print("get2", sitters)
        # Run the data through the serializer
        data = SitterSerializer(sitters, many=True).data
        print("get3")
        return Response({ 'sitters': data })

    def post(self, request):
        
        user = request.user
        sitter_data = Sitter(owner = user)
        sitter = SitterSerializer(sitter_data, data=request.data)
        if sitter.is_valid():
            # Save the created mango & send a response
            sitter.save()
            return Response(sitter.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(sitter.errors, status=status.HTTP_400_BAD_REQUEST)

class SitterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=()
    serializer_class = SitterSerializer
    def get(self, request, pk):
        """Show request"""
        # Locate the sitter to show
        sitter = get_object_or_404(Sitter, pk=pk)
        # Only want to show hired sitter?
        # if request.user != sitter.pet_owner:
        #     raise PermissionDenied('Unauthorized, you did not hire this sitter')
        data = SitterSerializer(sitter).data
        return Response({ 'sitter': data })

#     def delete(self, request, pk):
#         """Delete request"""
#         # Locate sitter to delete
#         sitter = get_object_or_404(Sitter, pk=pk)
#         # Check the pet's owner against the user making this request
#         if request.user != sitter.pet_owner:
#             raise PermissionDenied('Unauthorized, you did not hire this sitter')
#         # Only delete if the user hired the sitter
#         sitter.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def partial_update(self, request, pk):
#         """Update Request"""
#         # Locate Sitter
#         # get_object_or_404 returns a object representation of our Pet
#         sitter = get_object_or_404(Sitter, pk=pk)
#         # Check the pets's owner against the user making this request
#         if request.user != sitter.pet_owner:
#             raise PermissionDenied('Unauthorized, you did not hire this sitter')
    
#         # Ensure the owner field is set to the current user's ID
#         # Validate updates with serializer
#         ms = SitterSerializer(sitter, data=request.data['sitter'], partial=True) 
#         if ms.is_valid():
#             # Save & send a 204 no content
#             ms.save()
#             return Response(ms.data)
#         # If the data is not valid, return a response with the errors
#         return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createreviewsReview(request, pk):
    user = request.user
    reviews = Reviews.objects.get(_id=pk)
    data = request.data

lif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            reviews=reviews,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
        )

        reviews = reviews.review_set.all()
        reviews.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        reviews.rating = total / len(reviews)
        reviews.save()

        return Response('Review Added')
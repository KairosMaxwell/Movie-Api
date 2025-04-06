

from rest_framework import permissions, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializer_file import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_Date')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title']  # Allow search by movie title
    filterset_fields = ['movie_title']  # Allow filtering by movie title
    ordering_fields = ['rating', 'created_Date']
    # permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()  # The model queryset to interact with
    serializer_class = ReviewSerializer  # The serializer for the review data
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this

    def get_object(self):
        """
        This method is used to retrieve the review instance for the given 'id'.
        You can customize it if you need more complex logic.
        """
        return super().get_object()


# reviews/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializer_file import ReviewSerializer

@api_view(['POST'])
def post_review(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    # Validate that the movie exists
    movie_id = request.data.get("movie")
    try:
        movie = Review.objects.get(id=movie_id)
    except Review.DoesNotExist:
        return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

    # Validate the review data using the serializer
    serializer = ReviewSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Review posted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

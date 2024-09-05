from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Review
from .serializers import ReviewSerializer
from .utils import get_movie_recommendations


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    

class RecommendationView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        recommended_movie_ids = get_movie_recommendations(user.id)

        recommended_movies = Movie.objects.filter(tmdb_id__in=recommended_movie_ids)
        serializer = MovieSerializer(recommended_movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

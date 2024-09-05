from django.contrib.auth import get_user_model
from django.db import models
from movies.models import Movie

User = get_user_model()

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.movie.title} - {self.user.username}'

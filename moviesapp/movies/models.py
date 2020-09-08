# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from statistics import mean
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    poster = models.ImageField(upload_to="images/posters/", default='images/posters/movie_camera.png')
    year = models.PositiveIntegerField(default=2019)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})

    def get_reviews(self):
        return Review.objects.filter(movie_id=self.id)

    def get_rating(self, *args, **kwargs):
        reviews = self.get_reviews()
        self.rating = round(mean([review.rating for review in reviews]), 1) if len(reviews) > 0 else None
        super().save(*args, **kwargs)
        return self.rating

        
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.movie.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.movie_id})
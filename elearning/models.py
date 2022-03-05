from django.db import models


class Instructor(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=30, unique=True)
    registration_date = models.DateField()
    num_of_published_courses = models.IntegerField()
    num_of_enrolled_students = models.IntegerField()
    average_review_rating = models.FloatField()
    num_of_reviews = models.IntegerField()

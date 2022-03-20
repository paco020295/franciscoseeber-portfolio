from django.db import models
from django_countries.fields import CountryField


class Review(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    average_score = models.PositiveIntegerField()

    skills = models.PositiveIntegerField()
    quality = models.PositiveIntegerField()
    availability = models.PositiveIntegerField()
    deadlines = models.PositiveIntegerField()
    communication = models.PositiveIntegerField()
    cooperation = models.PositiveIntegerField()

    start_date = models.DateField()
    end_date = models.DateField()
    review_text = models.TextField(max_length=700, blank=True, default='')

    client_country = CountryField(blank_label='(select country)', max_length=50)
    client_city = models.CharField(max_length=100, blank=True)
    client_name = models.CharField(max_length=100, blank=True)

    client_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    client_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.title


from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime
def current_year():
    return datetime.date.today().year
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
from model_utils import Choices
Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)
Status = Choices (
    ('read'),
    ('want_to_read'),
    ('in_progress'),
    ('not_read')
)
class publish_house(models.Model):
    name = models.CharField(max_length=60, unique=True)
    address = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=60)

    def __str__(self):
        return self.name
class genre(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name
		
class country(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, unique=True)
    born_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)	
    country = models.ForeignKey(country)

    def __str__(self):
        return self.nickname
		
class book(models.Model):
    name = models.CharField(max_length=60)
    publish_house = models.ForeignKey(publish_house,default='', null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(blank=True)
    file = models.FileField(unique=True)
    page = models.PositiveIntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    description_of_book = models.CharField(max_length=255, unique=True)
    genre = models.ManyToManyField(genre)
    author = models.ManyToManyField(author)	
    def __str__(self):
        return self.name
		
class reader_book(models.Model):
    rating = models.IntegerField(choices=Rating_CHOICES, blank=True, null=True)
    upload_date = models.DateField(default=date.today)
    status = models.CharField(choices=Status, default=Status.not_read, max_length=12)
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(book)

    def __str__(self):
        return self.status
		
class comment(models.Model):
    posted = models.DateField(default=date.today)
    comment = models.CharField(max_length=120)
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(book)
    def __str__(self):
        return self.comment
		

		
		


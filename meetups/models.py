from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)


    def __str__(self):
        return f'{self.name} - {self.address}'


class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(blank=True)
    date = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'
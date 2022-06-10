from django.db import models

# Create your models here.
class Cat(models.Model):

    breed = models.CharField(max_length=200, unique=True)
    origin = models.CharField(max_length=250)
    occurrence = models.CharField(max_length=250)
    body_type = models.CharField(max_length=200)
    coat_type_and_length = models.CharField(max_length=200)
    coat_pattern = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    intro = models.TextField()
    description = models.TextField()
    history = models.TextField()

    def __str__(self) -> str:
        
        return f'Breed: {self.breed}'

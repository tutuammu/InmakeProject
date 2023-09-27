from django.db import models

# Create your models here.
class blow(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='flowers')
    desc = models.TextField()

    def __str__(self):
        return self.name

class high(models.Model):
    nam = models.CharField(max_length=150)
    img = models.ImageField(upload_to='images')
    des = models.TextField()
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.TextField()
    link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title

from django.db import models
from django.utils.text import slugify

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
    category = models.CharField(max_length=50, choices=[
        ('app', 'App'),
        ('card', 'Card'),
        ('web', 'Web'),
    ])
    image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
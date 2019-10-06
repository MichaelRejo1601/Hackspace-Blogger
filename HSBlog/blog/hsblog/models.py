from django.db import models

# Create your models here.
class Post(models.Model):
    """A topic the user is learning about"""
    date = models.DateField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    def __str__(self):
        """Return a string representation of the model."""
        return self.title

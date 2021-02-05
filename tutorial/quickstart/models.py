from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Movie(models.Model):

    artist = models.CharField(max_length=200, blank=True, null=True)
    alumb = models.CharField(max_length=200, blank=True, null=True)
 

    def __str__(self):
        return str(self.artist)


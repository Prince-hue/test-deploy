from django.db import models

# Create your models here.
class deploy(models.Model):
    name_of_websites = models.CharField(max_length=225)
    
    def __str__(self):
        return self.name_of_websites
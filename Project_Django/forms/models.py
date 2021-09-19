from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.
class new_Forms(models.Model):
    Name = models.CharField(max_length=124)
    Email = models.EmailField()
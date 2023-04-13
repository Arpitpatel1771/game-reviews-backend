from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class TestClass(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, choices=(("A", "A"),("B", "B")), 
                            help_text="Name of an entity in this model. E.g.: Arpit")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name="test", blank=True)
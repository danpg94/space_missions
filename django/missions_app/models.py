from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SpaceMission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title + " by " + self.user.username
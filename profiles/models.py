from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = ImageField(upload_to="images/", default="../defaultfilename-getfromcloudinary")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Profile"

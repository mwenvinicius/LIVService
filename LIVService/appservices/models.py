from django.db import models
import uuid

# Create your models here.

class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    instagramLink = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.title
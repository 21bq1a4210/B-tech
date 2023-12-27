# myapp/models.py
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/uploded')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description

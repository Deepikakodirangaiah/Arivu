from django.db import models

# Create your models here.
from django.db import models

class SpiritualTalk(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.speaker}"
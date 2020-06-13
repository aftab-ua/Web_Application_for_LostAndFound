from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Reward(models.Model):
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-update']


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=120)
    video = EmbedVideoField()  # same like models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
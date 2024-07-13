from django.db import models
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=100 )
    video = models.FileField(upload_to='video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mp3', 'AVI', 'WMV', 'png', 'jpg',]) 
    ])

    def __str__(self):
        return self.title
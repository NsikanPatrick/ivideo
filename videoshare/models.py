from django.db import models
# from pytz import timezone
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    vid_file = models.FileField(upload_to="uploads/video_files", validators = [FileExtensionValidator(allowed_extensions=['mp4'])])
    cover_thumbnail = models.FileField(upload_to="uploads/cover_thumbnails", validators = [FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    date_posted = models.DateTimeField(default=timezone.now())
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)




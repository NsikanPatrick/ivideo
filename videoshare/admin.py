from csv import list_dialects
from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'vid_file', 'cover_thumbnail', 'date_posted')

admin.site.register(Video, VideoAdmin)



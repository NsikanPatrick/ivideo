# Generated by Django 4.0.6 on 2022-08-03 19:34

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('vid_file', models.FileField(upload_to='uploads/video_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('cover_thumbnail', models.FileField(upload_to='uploads/cover_thumbnails', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2022, 8, 3, 19, 34, 21, 430909, tzinfo=utc))),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
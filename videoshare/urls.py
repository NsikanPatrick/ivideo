from django.urls import path
from . import views as video_views
from .views import CreateVideo, VideoDetail, UpdateVideo, DeleteVideo, AboutView


urlpatterns = [
    path('create/', CreateVideo.as_view(), name='create-video'),
    path('<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='update-video'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='delete-video'),
    path('about/', AboutView.as_view(), name='about-view'),
]

from venv import create
from wsgiref.handlers import format_date_time
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Video 
# Restricting certain permissions to only logged in users
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(ListView):
    model = Video
    template_name = "index.html"
    order_by = "-date_posted"


class AboutView(TemplateView):
    template_name = "create_video.html"

# Restricting the create video page to only logged in users
class CreateVideo(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'vid_file', 'cover_thumbnail']
    template_name = "reg.html"

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})


class VideoDetail(DetailView):
    model = Video
    template_name = "video_detail.html"

# Restricting the update video page to only logged in users
class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = "reg.html"

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader

# Restricting the delete video page to only logged in users
class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = "delete_video.html"

    def get_success_url(self):
        return reverse("index")

    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader
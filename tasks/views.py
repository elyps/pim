from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

from .models import Task

class TaskListView(ListView):
    model = Task
    queryset = Task.objects.all().order_by("-date_created").reverse()

class TaskListViewLast(ListView):
    model = Task
    queryset = Task.objects.all().order_by("-date_created").reverse()[:3]

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    fields = ["title", "content"]
    success_url = reverse_lazy("task-list")
    success_message = "Your new task was created!"

class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    fields = ["title", "content"]
    success_message = "Your task was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "task-detail",
            kwargs={"pk": self.task.id}
        )

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")
    success_message = "Your task was deleted!"

    def delete(self, request, *args, **kwargs):
        message.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


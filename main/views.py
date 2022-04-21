from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from tasks.models import Task


# Create your views here.
def main_index(request):
    if request.user.is_authenticated:
        return render(request, 'main/main_index.html')
    else:
        return redirect('auth0/signin')


def TaskListView(request):
    context = {}
    task = Task.objects.all()
    context['task_list'] = task
    return render(request, 'tasks/task_list.html', context)


class TaskListViewLast(ListView):
    model = Task
    template_name = "task_list.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_list.html"

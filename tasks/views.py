from django.shortcuts import render

from tasks.models import Task, Tag


def index(request):
    context = {
        "tasks": Task.objects.all().order_by("is_done", "-created_at" ),
        "tags": Tag.objects.all(),
    }
    return render(request, "tasks/index.html", context)
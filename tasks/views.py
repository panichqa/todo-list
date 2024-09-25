from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


def index(request):
    context = {
        "tasks": Task.objects.all().order_by("is_done", "-created_at" ),
    }
    return render(request, "tasks/index.html", context)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:index")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save(update_fields=["is_done"])
    return redirect("tasks:index")


def task_undo(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save(update_fields=["is_done"])
    return redirect("tasks:index")


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tasks/tag_list.html", {"tags": tags})


def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")
    else:
        form = TagForm()
    return render(request, "tasks/tag_form.html", {"form": form})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tasks:tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "tasks/tag_form.html", {"form": form})


def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("tasks:tag_list")
    return render(request, 'tasks/tag_confirm_delete.html', {"tag": tag})

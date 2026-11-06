from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task


@login_required
def task_list(request):
    return redirect("tasks:user_list", user_id=request.user.pk)


@login_required
def user_task_list(request, user_id):
    list_owner = get_object_or_404(get_user_model(), pk=user_id)
    #A01, Fix:
    #if user_id != request.user.pk:
    #    raise Http404

    tasks = Task.objects.filter(owner_id=user_id)
    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks, "form": TaskForm(), "list_owner": list_owner},
    )


@login_required
@require_POST
def create_task(request):
    form = TaskForm(request.POST)
    if not form.is_valid():
        tasks = Task.objects.filter(owner=request.user)
        return render(
            request,
            "tasks/task_list.html",
            {"tasks": tasks, "form": form, "list_owner": request.user},
            status=400,
        )
    task = form.save(commit=False)
    task.owner = request.user
    task.save()
    return redirect("tasks:user_list", user_id=request.user.pk)


@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, owner=request.user)
    # A09: Fix
    # logger.warning("Task deleted: task_id=%s actor=%s", task.pk, request.user.get_username())
    task.delete()
    return redirect("tasks:user_list", user_id=request.user.pk)

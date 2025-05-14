# projects/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Task
from .forms import ProjectForm
from .models import Project
from .forms import TaskForm

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})


def dashboard(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/dashboard.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.owner = request.user
            task.save()
            return redirect('project_detail', pk=project.id)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})


@login_required
def task_update_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            task.save()
    return redirect('project_detail', pk=task.project.id)

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'project': task.project})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    project_id = task.project.id
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project_id)
    return render(request, 'projects/task_confirm_delete.html', {'task': task})


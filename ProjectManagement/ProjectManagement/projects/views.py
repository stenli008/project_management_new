from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
import json

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.projects.forms import CreateProjectForm, CreateTaskForm, EditTaskForm
from ProjectManagement.projects.models import Project, Task, Client


def is_superuser(user):
    return user.is_superuser


def projects_landing_page_view(request):
    return render(request, 'projects/projects-landing-page.html')


@user_passes_test(is_superuser)
def projects_staff_page_view(request):
    workers = WorkerUser.objects.all()
    context = {
        'workers': workers,
    }
    return render(request, 'projects/projects-staff-page.html', context)


@user_passes_test(is_superuser)
def projects_projects_page_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects-projects-page.html', context)


@user_passes_test(is_superuser)
def projects_project_page_view(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'projects/projects-project-page.html', context)


@user_passes_test(is_superuser)
def projects_task_manage_page_view(request, slug):
    task = Task.objects.get(slug=slug)
    workers = task.workers.all()
    unused_workers = WorkerUser.objects.exclude(tasks=task)
    context = {
        'task': task,
        'workers': workers,
        'unused_workers': unused_workers,
    }
    return render(request, 'projects/projects-task-manage-page.html', context)


@user_passes_test(is_superuser)
def projects_new_project_page_view(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects-projects-page')
    else:
        form = CreateProjectForm()

    context = {
        'form': form,
        'clients': clients,
    }
    return render(request, 'projects/projects-new-project-page.html', context)


@user_passes_test(is_superuser)
def projects_new_task_page_view(request, slug):
    current_project = Project.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = current_project
            task.save()
            return redirect('projects-project-page', slug=current_project.slug)
    else:
        form = CreateTaskForm(initial={'project': current_project})

    context = {
        'form': form,
        'current_project': current_project,
    }
    return render(request, 'projects/projects-new-task-page.html', context)


@login_required()
def projects_worker_tasks_page_view(request, slug):
    worker = WorkerUser.objects.get(slug=slug)
    tasks = Task.objects.all().filter(workers=worker)
    context = {
        'worker': worker,
        'tasks': tasks,
    }
    return render(request, 'projects/projects-worker-tasks-page.html', context)


@user_passes_test(is_superuser)
def projects_edit_task_page_view(request, slug):
    task = Task.objects.get(slug=slug)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('projects-task-manage-page', slug=task.slug)
    else:
        form = EditTaskForm(instance=task)

    context = {
        'form': form
    }
    return render(request, 'projects/projects-edit-task-page.html', context)


@login_required()
def schedule_view(request):
    tasks = Task.objects.all()  # Fetch tasks from the database
    events = []

    for task in tasks:
        event = {
            'title': f'{task.project.project_name} - {task.task_category.name} - {task.requirement}',
            'start': task.date_added.strftime('%Y-%m-%d'),
            'end': task.deadline.strftime('%Y-%m-%d'),

        }
        events.append(event)

    context = {
        'events': json.dumps(events)  # Convert events array to JSON
    }
    return render(request, 'projects/schedule.html', context)

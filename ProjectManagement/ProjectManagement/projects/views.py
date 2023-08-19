from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.projects.models import Project, Task


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
    context = {
        'task': task,
    }
    return render(request, 'projects/project-task-manage-page.html', context)

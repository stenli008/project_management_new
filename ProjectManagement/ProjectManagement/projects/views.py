from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def projects_landing_page_view(request):
    return render(request, 'projects/projects-landing-page.html')

from django.shortcuts import render


def projects_landing_page_view(request):
    return render(request, 'projects/projects-landing-page.html')

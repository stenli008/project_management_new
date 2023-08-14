from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ProjectManagement.projects.forms import LeaveApplicationForm


def projects_landing_page_view(request):
    return render(request, 'projects/projects-landing-page.html')


@login_required
def projects_faqs_page_view(request):
    return render(request, 'projects/projects-faqs-page.html')


@login_required
def leave_requests_page_view(request):
    worker = request.user
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.worker = worker
            leave.save()
            return redirect('projects-faq-page')
    else:
        form = LeaveApplicationForm()

    context = {
        'form': form,
        'worker': worker,
    }

    return render(request, 'projects/leave-requests-page.html', context)

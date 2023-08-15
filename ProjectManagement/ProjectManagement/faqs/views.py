from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ProjectManagement.faqs.forms import LeaveApplicationForm, OtherApplicationForm


@login_required
def faqs_page_view(request):
    return render(request, 'faqs/faqs-page.html')


@login_required
def leave_requests_page_view(request):
    worker = request.user
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.worker = worker
            leave.save()
            return redirect('faqs-page')
    else:
        form = LeaveApplicationForm()

    context = {
        'form': form,
        'worker': worker,
    }

    return render(request, 'faqs/faqs-leave-requests-page.html', context)


@login_required
def other_requests_page_view(request):
    worker = request.user
    if request.method == 'POST':
        form = OtherApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.worker = worker
            application.save()
            return redirect('projects-landing-page')
    else:
        form = OtherApplicationForm()

    context = {
        'worker': worker,
        'form': form,
    }

    return render(request, 'faqs/faqs-other-requests-page.html', context)


@login_required
def annual_statement_page_view(request):
    worker = request.user
    context = {
        'worker': worker,
    }
    return render(request, 'faqs/faqs-annual-statement-page.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Project
from core.models import SiteSettings


def project_list(request):
    projects = Project.objects.all()
    site_settings = SiteSettings.objects.first()

    context = {
        'projects': projects,
        'site_settings': site_settings,
    }
    return render(request, 'projects/project_list.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    site_settings = SiteSettings.objects.first()

    context = {
        'project': project,
        'site_settings': site_settings,
    }
    return render(request, 'projects/project_detail.html', context)
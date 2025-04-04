from django.shortcuts import render
from .models import SiteSettings
from services.models import Service
from projects.models import Project


def index(request):
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()[:6]
    latest_projects = Project.objects.all()[:3]

    context = {
        'site_settings': site_settings,
        'services': services,
        'latest_projects': latest_projects,
    }
    return render(request, 'core/index.html', context)


def about(request):
    site_settings = SiteSettings.objects.first()

    context = {
        'site_settings': site_settings,
    }
    return render(request, 'core/about.html', context)

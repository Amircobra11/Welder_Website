from django.shortcuts import render
from .models import Service
from core.models import SiteSettings


def service_list(request):
    services = Service.objects.all()
    site_settings = SiteSettings.objects.first()

    context = {
        'services': services,
        'site_settings': site_settings,
    }
    return render(request, 'services/service_list.html', context)
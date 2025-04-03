from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from core.models import SiteSettings


def contact(request):
    site_settings = SiteSettings.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.')
            return redirect('contact:contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'site_settings': site_settings,
    }
    return render(request, 'contact/contact.html', context)
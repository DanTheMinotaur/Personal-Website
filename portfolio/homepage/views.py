from django.shortcuts import render
from django.http import HttpResponse

from .models import HomepageLink


def home(request):
    all_links = HomepageLink.objects.all()

    context = {
        'all_links': all_links,
        'page_title': "Home",

    }

    return render(request, 'homepage/home.html', context)

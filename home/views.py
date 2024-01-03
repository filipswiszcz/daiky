from django.shortcuts import render, get_object_or_404
from django.template import loader

from home.models import (
    Language
)


def index(request):
    return render(request, 'index.html')

def language(request):
    lang = Language.objects.get(id=1)
    context = {
        'lang': lang
    }
    return render(request, 'profile.html', context)
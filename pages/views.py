from django.shortcuts import render
from masterclasses.models import MasterClass
from library.models import Idea

def home(request):
    # Последние 3 мастер-класса (по дате проведения)
    latest_masterclasses = MasterClass.objects.filter(is_active=True).order_by('-schedule')[:3]
    # Последние 3 опубликованные идеи
    latest_ideas = Idea.objects.filter(is_published=True).order_by('-created_at')[:3]
    context = {
        'latest_masterclasses': latest_masterclasses,
        'latest_ideas': latest_ideas,
    }
    return render(request, 'pages/home.html', context)
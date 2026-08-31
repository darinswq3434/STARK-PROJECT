from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Armor, Technology, Actor

def index(request):
    return render(request, 'suits/index.html')

def about(request):
    return render(request, 'suits/about.html')

def armor(request):
    armors = Armor.objects.all()
    return render(request, 'suits/armor.html', {'armors': armors})

def technologies(request):
    technologies = Technology.objects.all()
    return render(request, 'suits/technologies.html', {'technologies': technologies})
def actor(request):
    actor = Actor.objects.all()
    return render(request, 'suits/actor.html', {'actor': actor})

def armor_detail(request, id):
    armor = get_object_or_404(Armor, id=id)
    return render(request, 'suits/armor_detail.html', {'armor': armor})

def actor(request):
    actors = Actor.objects.all()

    return render(request, 'suits/actor.html', {
        'actors': actors
    })
    
    
def technology_detail(request, id):
    technology= get_object_or_404(Technology, id=id)
    return render(request, 'suits/technology_detail.html', {'technology':technology})


def history(request):
    return render(request, 'suits/history.html')

def archive(request):
    return render(request, 'suits/archive.html')
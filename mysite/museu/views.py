from django.shortcuts import render
from .models import Messages


def index(request):
    return render(request, 'museu/index.html')


def check_db(request):
    return render(request, 'museu/check_db.html', {'messages': Messages.objects.all()})

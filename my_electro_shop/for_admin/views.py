from django.shortcuts import render
from .models import Card_with_description

def registration(request):
    news = Card_with_description.objects.all()
    return render(request, "for_admin/registration.html", {'news' : news})

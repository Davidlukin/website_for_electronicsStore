from django.shortcuts import render
from .models import TraidIns

def index(request):
    return render(request, 'main/index.html')

def info(request):
    return render(request, 'main/info.html')

def contact(request):
    return render(request, 'main/contact.html')

def pickup(request):
    return render(request, 'main/pickup.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def payment(request):
    return render(request, 'main/payment.html')

def grade(rquest):
    return render(rquest,'main/grade.html')

def submit_form(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        state = request.POST['state']
        model_name = request.POST['model_name']

        TraidIns.objects.create(phone_number=phone_number, state=state, model_name=model_name)
        return render(request, 'main/success.html')

    return render(request, 'main/grade.html')

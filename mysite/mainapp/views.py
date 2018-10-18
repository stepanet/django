from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Есть вопросы??','tel:222-22-22','email:dimadd@mail.ru']})

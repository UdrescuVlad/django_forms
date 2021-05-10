from django.shortcuts import render

# Create your views here.

def home1(request):
    return render(request, 'pizza/home.html')


def order(request):
    return render(request, 'pizza/order.html')
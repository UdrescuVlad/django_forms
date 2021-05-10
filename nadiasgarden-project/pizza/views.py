from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.

def home1(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', {'pizzaform':form})
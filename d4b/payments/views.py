from django.shortcuts import render
from .payments_data import payments
from .helpers import todaysPayments, yesterdaysPayments, thisWeeksPayments

# Create your views here.
def index(request):
    context = {
        "payments": payments
    }
    
    return render(request, 'payments.html', context)

def today(request):
    context = {
        "payments": todaysPayments(payments)
    }

    return render(request, 'payments.html', context)

def yesterday(request):
    context = {
        "payments": yesterdaysPayments(payments)
    }

    return render(request, 'payments.html', context)

def thisWeek(request):
    context = {
        "payments": thisWeeksPayments(payments)
    }

    return render(request, 'payments.html', context)
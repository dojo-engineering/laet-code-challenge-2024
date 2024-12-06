from django.shortcuts import render
from .payments_data import payments_data
from .helpers import sortPaymentsByDate, sumPayments, searchPayments, todaysPayments, yesterdaysPayments, thisWeeksPayments

# Create your views here.
def index(request):
    payments = sortPaymentsByDate(payments_data)
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "page_name": "All payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total": sumPayments(paymentsToShow),
    }
    
    return render(request, 'payments.html', context)

def today(request):
    payments = todaysPayments(sortPaymentsByDate(payments_data))
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "page_name": "Today's payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total": sumPayments(paymentsToShow),
    }

    return render(request, 'payments.html', context)

def yesterday(request):
    payments = yesterdaysPayments(sortPaymentsByDate(payments_data))
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "page_name": "Yesterday's payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total": sumPayments(paymentsToShow),
    }

    return render(request, 'payments.html', context)

def thisWeek(request):
    payments = thisWeeksPayments(sortPaymentsByDate(payments_data))
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "page_name": "This week's payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total": sumPayments(paymentsToShow),
    }

    return render(request, 'payments.html', context)

def take_a_payment(request):
    paymentsToShow = sortPaymentsByDate(payments_data)

    context = {
        "page_name": "All payments",
        "payments": paymentsToShow,
        "search": "",
        "status": "",
        "total": sumPayments(paymentsToShow),
        "dialog": True,
    }
    
    return render(request, 'payments.html', context)
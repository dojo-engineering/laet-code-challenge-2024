from django.shortcuts import render
from django.views import View

from .forms import TakePaymentForm
from .payments_data import Payment, payments_data
from .helpers import sortPaymentsByDate, sumPayments, searchPayments, todaysPayments, yesterdaysPayments, thisWeeksPayments, refundPayments

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
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow)
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
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow)
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
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow)
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
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow)
    }

    return render(request, 'payments.html', context)

def take_a_payment(request):

    if request.method == 'POST':
        print("POST")
        print(request.POST.get('value_input', ''))
        print(request.POST.get('payment_type_input', ''))

        new_payment = Payment(int(request.POST.get('value_input', '')), '2024-12-10',request.POST.get('payment_type_input', ''), "Success", )
        payments_data.append(new_payment)
        
    form = TakePaymentForm()
    paymentsToShow = sortPaymentsByDate(payments_data)

    context = {
        "page_name": "All payments",
        "payments": paymentsToShow,
        "search": "",
        "status": "",
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow),
        "dialog": True,
        "take_payment_screen": " ",
        "payment_form": form
    }
    
    return render(request, 'payments.html', context)

def tasks(request): 
    return render(request, 'tasks.html')

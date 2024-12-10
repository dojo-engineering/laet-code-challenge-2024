from django.shortcuts import render
from django.views import View

from .forms import TakePaymentForm
from .payments_data import Payment, payments_data
from .helpers import refundPayment, sortPaymentsByDate, calculateTotalTakings, searchPayments, todaysPayments, yesterdaysPayments, thisWeeksPayments, calculateRefunds

def index(request):
    refundId = request.GET.get('refund') if 'refund' in request.GET else ""

    if refundId:
        refundPayment(payments_data, refundId)

    payments = sortPaymentsByDate(payments_data)
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "path": "/",
        "page_name": "All Payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total_takings": calculateTotalTakings(paymentsToShow),
        "total_refunds": calculateRefunds(paymentsToShow)
    }
    
    return render(request, 'payments.html', context)

def today(request):
    refundId = request.GET.get('refund') if 'refund' in request.GET else ""

    if refundId:
        refundPayment(payments_data, refundId)

    payments = todaysPayments(sortPaymentsByDate(payments_data))
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "path": "/today",
        "page_name": "Today's Payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total_takings": calculateTotalTakings(paymentsToShow),
        "total_refunds": calculateRefunds(paymentsToShow)
    }

    return render(request, 'payments.html', context)

def yesterday(request):
    refundId = request.GET.get('refund') if 'refund' in request.GET else ""

    if refundId:
        refundPayment(payments_data, refundId)

    payments = yesterdaysPayments(sortPaymentsByDate(payments_data))
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "path": "/yesterday",
        "page_name": "Yesterday's Payments",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total_takings": calculateTotalTakings(paymentsToShow),
        "total_refunds": calculateRefunds(paymentsToShow)
    }

    return render(request, 'payments.html', context)

def thisWeek(request):
    refundId = request.GET.get('refund') if 'refund' in request.GET else ""

    if refundId:
        refundPayment(payments_data, refundId)
        
    payments = thisWeeksPayments(sortPaymentsByDate(payments_data))
    search = request.GET.get('search') if 'search' in request.GET else ""
    status = request.GET.get('status') if 'status' in request.GET else ""
    
    paymentsToShow = searchPayments(payments, search, status)

    context = {
        "path": "/this-week",
        "page_name": "Payments This Week",
        "payments": paymentsToShow,
        "search": search,
        "status": status,
        "total_takings": calculateTotalTakings(paymentsToShow),
        "total_refunds": calculateRefunds(paymentsToShow)
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
        "path": "/take-a-payment",
        "page_name": "All Payments",
        "payments": paymentsToShow,
        "search": "",
        "status": "",
        "total_takings": calculateTotalTakings(paymentsToShow),
        "total_refunds": calculateRefunds(paymentsToShow),
        "dialog": True,
        "take_payment_screen": " ",
        "payment_form": form
    }
    
    return render(request, 'payments.html', context)

def tasks(request):
    context = {
        "path": "/tasks",
    }

    return render(request, 'tasks.html', context)

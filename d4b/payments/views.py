from django.shortcuts import render
from django.views import View
from .payments_data import Payment, payments_data
from .helpers import sortPaymentsByDate, sumPayments, searchPayments, todaysPayments, yesterdaysPayments, thisWeeksPayments, refundPayments

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
    paymentsToShow = sortPaymentsByDate(payments_data)
    temp = TakePayment()

    context = {
        "page_name": "All payments",
        "payments": paymentsToShow,
        "search": "",
        "status": "",
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow),
        "dialog": True,
        "take_payment_screen": " "
    }
    
    return render(request, 'payments.html', context)


class TakePayment(View): 

    def __init__(self):
        self.value = '' 
    
    def get(self, request, number, current_val): 
        if ('button' in request.path):
            self.buttonPressed(number, current_val)
        elif ('back' in request.path):
            self.backButton(current_val)
        elif('enter' in request.path):
            self.enterButton(current_val)
        return self.render(request)
    
    def buttonPressed(self, number, current_val): 
        self.value += (current_val + number)
        print(self.value)

    def backButton(self, current_val): 
        try: 
            print(current_val)
            print(current_val[1])
            self.value = current_val[:-1]
        except:
            self.value = " " 

    def enterButton(self, current_val):
        new_payment = Payment(current_val, "2025-11-25", "Visa", "Success")
        payments_data.append(new_payment)
        self.value = " "
    
    def render(self, request): 
        paymentsToShow = sortPaymentsByDate(payments_data)
        context = {
        "page_name": "All payments",
        "payments": paymentsToShow,
        "search": "",
        "status": "",
        "total_takings": sumPayments(paymentsToShow),
        "total_refunds": refundPayments(paymentsToShow),
        "dialog": True,
        "take_payment_screen": self.value
    }
    
        return render(request, 'payments.html', context)
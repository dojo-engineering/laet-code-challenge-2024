from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today', views.today, name='today'),
    path('yesterday', views.yesterday, name='yesterday'),
    path('this-week', views.thisWeek, name='this-week'),
    path('take-a-payment', views.take_a_payment, name='take-a-payment'),
    path('button/<str:number>/<str:current_val>', views.TakePayment.as_view(), name='button'),
    path('back/<str:number>/<str:current_val>', views.TakePayment.as_view(), name='back'),
    path('enter/<str:number>/<str:current_val>', views.TakePayment.as_view(), name='enter'),
]
from django import forms


class TakePaymentForm(forms.Form): 
    value_input = forms.CharField(label='Input Value', required=True)
    payment_type_input = forms.CharField(label='Input Payment Type', required=True)
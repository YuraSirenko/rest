from django import forms

from .models import Customer, Waiter, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birth_date', 'phone', 'sale']

class WaiterForm(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = ['first_name', 'last_name', 'birth_date', 'phone', 'hire_date', 'salary_type']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table', 'customer', 'number_of_customers']
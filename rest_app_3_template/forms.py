from django import forms
from django.forms import formset_factory
from .repositories.customer_repository import CustomerRepository
from .repositories.payment_method_repository import PaymentMethodRepository
from .repositories.order_repository import OrderRepository
from .repositories.item_repository import ItemRepository

class CustomerModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name

class PaymentModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.payment_type

class OrderForm(forms.Form):
    table_id = forms.IntegerField()
    customer = CustomerModelChoiceField(queryset=CustomerRepository().get_all())
    number_of_customers = forms.IntegerField()
    total_sum = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    event_started = forms.DateTimeField(required=False)
    event_ended = forms.DateTimeField(required=False)
    payment_method = PaymentModelChoiceField(queryset=PaymentMethodRepository().get_all(), required=False)

    def save(self, commit=True):
        data = self.cleaned_data
        order = OrderRepository().create(
            table_id=data['table_id'],
            customer_id=data['customer'].id,
            number_of_customers=data['number_of_customers'],
            payment_method=data['payment_method'],
            total_sum=data['total_sum'],
            event_started=data['event_started'],
            event_ended=data['event_ended']
        )
        return order

class ItemHasOrderChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ItemHasOrderForm(forms.Form):
    item = ItemHasOrderChoiceField(queryset=ItemRepository().get_all())
    quantity = forms.IntegerField(min_value=1)

ItemHasOrderFormSet = formset_factory(ItemHasOrderForm, extra=1)

from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from .repositories.order_repository import OrderRepository
from .repositories.item_has_order_repository import ItemHasOrderRepository

from .forms import OrderForm
from .forms import ItemHasOrderFormSet
from .services.item_has_order_service import ItemHasOrderService
from .repositories.waiter_repository import WaiterRepository
from django.http import JsonResponse
from rest_app_3_template.NetworkHelper import NetworkHelper

waiter_repository = WaiterRepository()
order_repository = OrderRepository()
item_has_order_repository = ItemHasOrderRepository()

network_helper = NetworkHelper(base_url='http://127.0.0.1:8080/', api_key='your_api_key_here')

def external_api_view(request):
    base_url = 'http://localhost:8080'  # URL of the other app
    api_key = 'your_api_key_here'  # Replace with your actual API key

    network_helper = NetworkHelper(base_url, api_key)

    # Example: Get a list of items from the other app
    items = network_helper.get_list('items')

    return JsonResponse(items, safe=False)
def order_list(request):
    orders = order_repository.get_all()
    for order in orders:
        order.number_of_waiters = order.waiters.count()
        order.number_of_items = order.items.count()
    return render(request, 'order_all.html', {"orders": orders})

def order_detail(request, order_id):
    order = order_repository.get_by_id(order_id)
    item_has_orders = item_has_order_repository.get_all().filter(order=order)
    order.waiters_list = order.waiters.all()
    order.items_list = []
    order.total_sum = 0

    for item_has_order in item_has_orders:
        item = item_has_order.item
        item.quantity = item_has_order.quantity
        order.total_sum += item.price * item.quantity
        order.items_list.append(item)
    return render(request, 'order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rest_app_3_template/order_all/')  # Change to the appropriate URL
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

def order_update(request, order_id):
    order = order_repository.get_by_id(order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rest_app_3_template/order_all/')  # Change to the appropriate URL
    else:
        form = OrderForm(initial={
            'table_id':order.table_id,
            'customer': order.customer_id,
            'number_of_customers': order.number_of_customers,
            'payment_method':order.payment_method,
            'total_sum': order.total_sum,
            'event_started': order.event_started,
            'event_ended': order.event_ended
            })
    return render(request, 'order_form.html', {'form': form})

def update_item_quantities(request, order_id):
    order = order_repository.get_by_id(order_id)
    item_has_orders = item_has_order_repository.get_all().filter(order=order)

    if request.method == 'POST':
        formset = ItemHasOrderFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                item = form.cleaned_data.get('item')
                quantity = form.cleaned_data.get('quantity')
                if item and quantity is not None:
                    existing_item = ItemHasOrderService.get_by_order_and_item(order, item)
                    if existing_item:
                        existing_item.quantity = quantity
                        existing_item.save()
                    else:
                        item_has_order_repository.create(order=order, item=item, quantity=quantity)
            return redirect(reverse('rest_app_3_template:order_detail', args=[order_id]))
        else:
            print(formset.errors)  # Log formset errors for debugging
    else:
        initial_data = [{'item': item_has_order.item, 'quantity': item_has_order.quantity, 'id': item_has_order.id} for item_has_order in item_has_orders]
        formset = ItemHasOrderFormSet(initial=initial_data)

    return render(request, 'update_item_quantities.html', {'formset': formset, 'order': order})

def delete_item(request, order_id, item_id):
    if request.method == 'POST':
        item_has_order_repository.delete(item_id)
    return redirect(reverse('rest_app_3_template:update_item_quantities', args=[order_id]))

def update_waiters(request, order_id):
    order = order_repository.get_by_id(order_id)
    waiters = waiter_repository.get_all()

    if request.method == 'POST':
        waiter_id = request.POST.get('waiter')
        waiter = waiter_repository.get_by_id(waiter_id)
        order.waiters.add(waiter)
        return redirect(reverse('rest_app_3_template:update_waiters', args=[order_id]))

    return render(request, 'update_waiters.html', {'order': order, 'waiters': waiters})

def remove_waiter(request, order_id, waiter_id):
    if request.method == 'POST':
        order = order_repository.get_by_id(order_id)
        waiter = waiter_repository.get_by_id(waiter_id)
        order.waiters.remove(waiter)
    return redirect(reverse('rest_app_3_template:update_waiters', args=[order_id]))

def order_delete(request, order_id):
    if request.method == 'POST':
        order = order_repository.get_by_id(order_id)
        order.delete()
        return redirect(reverse('rest_app_3_template:order_all'))

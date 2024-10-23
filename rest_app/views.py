from django.shortcuts import render, redirect

from .models import ItemHasOrder

from .repositories.customer_repository import CustomerRepository
from .forms import CustomerForm

from .repositories.waiter_repository import WaiterRepository
from .forms import WaiterForm

from .repositories.order_repository import OrderRepository
from .forms import OrderForm
customer_repository = CustomerRepository()
waiter_repository = WaiterRepository()
order_repository = OrderRepository()
def customer_all(request):
    customers = customer_repository.get_all()
    return render(request, 'customer_all.html', {'customers': customers})
def customer_detail(request, Oid):
    customer = customer_repository.get_by_id(Oid)
    return render(request, 'customer_detail.html', {'customer': customer})
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = customer_repository.add(form.save())
            return redirect(f'/customer/{customer.id}')
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})
def waiter_all(request):
    waiters = waiter_repository.get_all()
    return render(request, 'waiter_all.html', {'waiters': waiters})
def waiter_detail(request, Oid):
    waiter = waiter_repository.get_by_id(Oid)
    return render(request, 'waiter_detail.html', {'waiter': waiter})
def waiter_add(request):
    if request.method == 'POST':
        form = WaiterForm(request.POST)
        if form.is_valid():
            waiter = waiter_repository.add(form.save())
            return redirect(f'/waiter/{waiter.id}')
    else:
        form = WaiterForm()
    return render(request, 'waiter_add.html', {'form': form})
def order_all(request):
    orders = order_repository.get_all()
    for order in orders:
        order.waiters_list = order.waiters.all()
        order.items_list = []
        for item_has_order in ItemHasOrder.objects.filter(order=order):
            item = item_has_order.item
            item.quantity = item_has_order.quantity
            order.items_list.append(item)

    return render(request, 'order_all.html', {'orders': orders})
def order_detail(request, Oid):
    order = order_repository.get_by_id(Oid)
    order.waiters_list = order.waiters.all()
    order.items_list = []
    order.total_sum = 0
    for item_has_order in ItemHasOrder.objects.filter(order=order):
        item = item_has_order.item
        item.quantity = item_has_order.quantity
        order.total_sum += item.price * item.quantity
        order.items_list.append(item)
    order.save()
    return render(request, 'order_detail.html', {'order': order})
def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = order_repository.add(form.save())
            return redirect(f'/order/{order.id}')
    else:
        form = OrderForm()
    return render(request, 'order_add.html', {'form': form})


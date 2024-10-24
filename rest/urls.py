from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_app.views import (
    CustomerViewSet, ItemViewSet, ItemHasOrderViewSet, ItemTypeViewSet, OrderViewSet,
    PaymentMethodViewSet, SalaryHistoryViewSet, SalaryTypeViewSet, SaleViewSet,
    TableInRestaurantViewSet, WaiterViewSet, WaiterHasOrderViewSet
)

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'items', ItemViewSet)
router.register(r'item-has-orders', ItemHasOrderViewSet)
router.register(r'item-types', ItemTypeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'salary-histories', SalaryHistoryViewSet)
router.register(r'salary-types', SalaryTypeViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'tables-in-restaurant', TableInRestaurantViewSet)
router.register(r'waiters', WaiterViewSet)
router.register(r'waiter-has-orders', WaiterHasOrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
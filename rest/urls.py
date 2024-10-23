"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer_all/', views.customer_all, name='customer_all'),
    path('customer/<int:Oid>/', views.customer_detail, name='customer_detail'),
    path('customer_add/', views.customer_add, name='customer_add'),
    path('waiter_all/', views.waiter_all, name='waiter_all'),
    path('waiter/<int:Oid>/', views.waiter_detail, name='waiter_detail'),
    path('waiter_add/', views.waiter_add, name='waiter_add'),
    path('order_all/', views.order_all, name='order_all'),
    path('order/<int:Oid>/', views.order_detail, name='order_detail'),
    path('order_add/', views.order_add, name='order_add'),
]
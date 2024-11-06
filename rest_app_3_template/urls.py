from django.contrib import admin
from django.urls import path
from rest_app_3_template import views
from .mate_views import FlightListView, FlightDetailView, PassengerListView, PassengerDetailView, PassengerDeleteView, FlightDeleteView

app_name = 'rest_app_3_template'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order_all/', views.order_list, name='order_all'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/update/<int:order_id>/', views.order_update, name='order_update'),
    path('order/<int:order_id>/update_item_quantities/', views.update_item_quantities, name='update_item_quantities'),
    path('order/<int:order_id>/delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('order/<int:order_id>/update_waiters/', views.update_waiters, name='update_waiters'),
    path('order/<int:order_id>/remove_waiter/<int:waiter_id>/', views.remove_waiter, name='remove_waiter'),
    path('order/<int:order_id>/delete/', views.order_delete, name='order_delete'),
    path('external-api/', views.external_api_view, name='external_api'),
    path('passengers/', PassengerListView.as_view(), name='passenger-list'),
    path('passengers/<int:passenger_id>/', PassengerDetailView.as_view(), name='passenger-detail'),
    path('passengers/<int:passenger_id>/delete/', PassengerDeleteView.as_view(), name='passenger-delete'),
    path('flights/', FlightListView.as_view(), name='flight-list'),
    path('flights/<int:flight_id>/', FlightDetailView.as_view(), name='flight-detail'),
    path('flights/<int:flight_id>/delete/', FlightDeleteView.as_view(), name='flight-delete'),
]
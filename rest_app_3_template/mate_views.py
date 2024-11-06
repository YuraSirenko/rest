# rest_app_3_template/mate_views.py
from django.views import View
from .NetworkHelper import NetworkHelper
from django.shortcuts import render, redirect

# Initialize NetworkHelper with your base URL and API key
network_helper = NetworkHelper(base_url='http://127.0.0.1:8080/', api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODYzNDgwLCJpYXQiOjE3MzA4NTYyODAsImp0aSI6ImUwYjYxYzNmYzNjMTQ2MmE4NDUxZDhlODFiZTgxOTJmIiwidXNlcl9pZCI6MX0.wX4qlSM__6Agw7QgCVG3NGo69Fk5SmSAx1usn3q1fnI')

class FlightDeleteView(View):
    def post(self, request, flight_id):
        success = network_helper.delete_flight(flight_id)
        return redirect('rest_app_3_template:flight-list')
class PassengerDeleteView(View):
    def post(self, request, passenger_id):
        success = network_helper.delete_passenger(passenger_id)
        return redirect('rest_app_3_template:passenger-list')
class FlightListView(View):
    def get(self, request):
        flights = network_helper.get_flights()
        return render(request, 'flights_list.html', {'flights': flights})

    def post(self, request):
        data = request.POST.dict()
        new_flight = network_helper.create_flight(data)
        return redirect('rest_app_3_template:flight-list')

class FlightDetailView(View):
    def get(self, request, flight_id):
        flight = network_helper.get_flight_by_id(flight_id)
        if flight is None:
            return redirect('rest_app_3_template:flight-list')
        return render(request, 'flight_detail.html', {'flight': flight})

    def post(self, request, flight_id):
        data = request.POST.dict()
        updated_flight = network_helper.update_flight_by_id(flight_id, data)
        return redirect('rest_app_3_template:flight-detail', flight_id=flight_id)



class PassengerListView(View):
    def get(self, request):
        passengers = network_helper.get_passengers()
        return render(request, 'passengers_list.html', {'passengers': passengers})

    def post(self, request):
        data = request.POST.dict()
        new_passenger = network_helper.create_passenger(data)
        return redirect('rest_app_3_template:passenger-list')

class PassengerDetailView(View):
    def get(self, request, passenger_id):
        passenger = network_helper.get_passenger_by_id(passenger_id)
        if passenger is None:
            return redirect('rest_app_3_template:passenger-list')
        return render(request, 'passenger_detail.html', {'passenger': passenger})

    def post(self, request, passenger_id):
        data = request.POST.dict()
        updated_passenger = network_helper.update_passenger_by_id(passenger_id, data)
        return redirect('rest_app_3_template:passenger-detail', passenger_id=passenger_id)
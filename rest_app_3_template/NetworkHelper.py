# rest_app_3_template/NetworkHelper.py
import requests

class NetworkHelper:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_passenger(self, data):
        response = requests.post(f"{self.base_url}/passengers/", headers=self.headers, json=data)
        print(f"Request data: {data}")  # Debug statement
        print(f"Response status code: {response.status_code}")  # Debug statement
        print(f"Response content: {response.content}")  # Debug statement
        if response.status_code == 201:
            return response.json()
        return None

    def create_flight(self, data):
        response = requests.post(f"{self.base_url}/flights/", headers=self.headers, json=data)
        if response.status_code == 201:
            return response.json()
        return None

    # Passengers
    def get_passengers(self):
        response = requests.get(f"{self.base_url}/passengers/", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def get_passenger_by_id(self, passenger_id):
        response = requests.get(f"{self.base_url}/passengers/{passenger_id}/", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def update_passenger_by_id(self, passenger_id, data):
        response = requests.put(f"{self.base_url}/passengers/{passenger_id}/", headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        return None



    # Flights
    def get_flights(self):
        response = requests.get(f"{self.base_url}/flights/", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def get_flight_by_id(self, flight_id):
        response = requests.get(f"{self.base_url}/flights/{flight_id}/", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def update_flight_by_id(self, flight_id, data):
        response = requests.put(f"{self.base_url}/flights/{flight_id}/", headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        return None

    def delete_flight(self, flight_id):
        response = requests.delete(f"{self.base_url}/flights/{flight_id}/", headers=self.headers)
        return response.status_code == 204

    def delete_passenger(self, passenger_id):
        response = requests.delete(f"{self.base_url}/passengers/{passenger_id}/", headers=self.headers)
        return response.status_code == 204
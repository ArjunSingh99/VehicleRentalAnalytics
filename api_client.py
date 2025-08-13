import requests

class ApiClient:
    def __init__(self, base_url: str, verify_ssl = False):
        self.base_url = base_url
        self.verify_ssl = verify_ssl
    
    def get_bookings(self):
        url = f'{self.base_url}/api/v1/bookings'

        response = requests.get(url, verify=self.verify_ssl)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch bookings: {response.status_code}")
    
    def get_location_history(self, base_url: str, booking_id: str, verify_ssl=False):
        url = f'{base_url}/api/v1/bookings/{booking_id}/location/history'

        response = requests.get(url, verify=verify_ssl)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch location history: {response.status_code}")
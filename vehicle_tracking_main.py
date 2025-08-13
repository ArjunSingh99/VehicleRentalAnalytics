import configparser
import sys
from api_client import ApiClient
from vehicle_tracking import Tracking

def main():
    print('Started Vehicle Tracking')
    if len(sys.argv) < 2:
        print("Usage: python vehicle_tracking_main.py <booking_id>")
        sys.exit(1)
    booking_id = sys.argv[1]

    config = configparser.ConfigParser()
    config.read('credentials.ini')
    base_url = config.get('API', 'BASE_URL', fallback='http://localhost:5047')
    verify_ssl = config.getboolean('API', 'VERIFY_SSL', fallback=False)

    client = ApiClient(base_url, verify_ssl)
    vehicle_data = client.get_location_history(base_url, booking_id, verify_ssl)
    tracking = Tracking(vehicle_data, map_centre=(50, -80))
    tracking.plot_vehicle_locations()

    print('Vehicle tracking completed')

if __name__ == '__main__':
    main()
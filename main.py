from api_client import ApiClient
from analytics import Analytics
from report_generator import Reporter

BASE_URL = 'http://localhost:5047'
VERIFY_SSL = False

def main():
    print('start')
    client = ApiClient(BASE_URL, VERIFY_SSL)

    bookings = client.get_bookings()

    analytics = Analytics(bookings)
    analytics_data, car_counts = analytics.analyze_bookings()

    # report gen
    Reporter.export_json(analytics_data)
    Reporter.export_csv(analytics_data, car_counts)
    Reporter.plot_car_popularity(car_counts)

    print('Analysis completed')

if __name__ == '__main__':
    main()
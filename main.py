import configparser
from api_client import ApiClient
from analytics import Analytics
from report_generator import Reporter

def main():
    print('Started Analysis')
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    base_url = config.get('API', 'BASE_URL', fallback='http://localhost:5047')
    verify_ssl = config.getboolean('API', 'VERIFY_SSL', fallback=False)

    client = ApiClient(base_url, verify_ssl)
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
from collections import Counter
from datetime import datetime

class Analytics:
    def __init__(self, bookings):
        self.bookings = bookings

    def analyze_bookings(self):
        total_revenue = 0
        booking_lengths = []
        car_models = []

        for booking in self.bookings:
            pickup_date = datetime.fromisoformat(booking['pickupDate'])
            return_date = datetime.fromisoformat(booking['returnDate'])

            days = (return_date - pickup_date).days + 1

            revenue = days * booking['dailyRate']
            total_revenue += revenue

            booking_lengths.append(days)
            car_models.append(booking['vehicleModel'])

        car_counts = Counter(car_models)

        most_popular_vehicle = car_counts.most_common(1)[0][0]
        
        avg_booking_length = sum(booking_lengths) / len(booking_lengths)

        analysis = {
            'total_revenue': total_revenue,
            'most_popular_vehicle_model': most_popular_vehicle,
            'average_booking_length_days': avg_booking_length
        }

        return analysis, car_counts
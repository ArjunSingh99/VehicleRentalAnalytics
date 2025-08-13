import json
import csv
import matplotlib.pyplot as plt

class Reporter:
    @staticmethod
    def export_json(data, filename='analytics.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    @staticmethod
    def export_csv(analytics, car_counts, filename='analytics.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Metric','Value'])

            for key, value in analytics.items():
                writer.writerow([key, value])
            
            writer.writerow([])

            writer.writerow(['Car Model', 'Number of Rentals'])
            for car, count in car_counts.items():
                writer.writerow([car, count])
            
    @staticmethod
    def plot_car_popularity(car_counts, filename='car_popularity_metrics.png'):
        cars = list(car_counts.keys())
        counts = list(car_counts.values())

        plt.figure(figsize=(8,5))
        plt.bar(cars, counts)
        plt.xlabel('Car Model')
        plt.ylabel('Number of Rentals')
        plt.title('Car Model Popularity')
        plt.savefig(filename)
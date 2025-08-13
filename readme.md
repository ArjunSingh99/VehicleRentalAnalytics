# Vehicle Rental Analytics

This project analyzes vehicle rental bookings and generates reports on revenue, booking lengths, and car model popularity.

## Requirements

- **Python 3.8+**
- The following Python packages (install via pip):

  ```
  pip install -r requirements.txt
  ```

  - `requests`
  - `matplotlib`
  - `folium`

## Configuration

- Set your API base URL and SSL verification in `credentials.ini`:
  ```
  [API]
  BASE_URL = http://localhost:5047
  VERIFY_SSL = False
  ```
  Change `BASE_URL` if your API is hosted elsewhere.
  Set `VERIFY_SSL` to `True` if your API uses a valid SSL certificate.

## How to Run

1. Ensure your API server is running and accessible at the configured `BASE_URL`.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the analytics:
   ```
   python main.py
   ```
4. Run vehicle tracking for a specific booking:
   ```
   python vehicle_tracking_main.py <booking_id>
   ```
   Replace `<booking_id>` with the actual booking ID you want to visualize.

## Output

- **analytics.json**: Summary of analytics in JSON format.
- **analytics.csv**: CSV report with metrics and car model counts.
- **car_popularity_metrics.png**: Bar chart showing car model popularity.
- **vehicle_tracking_map.html**: Interactive map showing vehicle locations (opened automatically in your browser).

## Project Structure

- `main.py` - Entry point for running analytics.
- `vehicle_tracking_main.py` - Entry point for vehicle tracking visualization.
- `api_client.py` - Handles API requests.
- `analytics.py` - Performs data analysis.
- `report_generator.py` - Generates reports (JSON, CSV, plots).
- `vehicle_tracking.py` - Handles vehicle tracking map generation.
- `requirements.txt` - Python dependencies.

## Notes

- Make sure your API provides booking data at `/api/v1/bookings`.
- For a compatible API implementation, see: [vehicle-rental-management](https://github.com/ArjunSingh99/vehicle-rental-management)

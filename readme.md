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

## Configuration

- The API base URL is set in `main.py`:
  ```
  BASE_URL = 'http://localhost:5047'
  ```
  Change this if your API is hosted elsewhere.
- SSL verification is disabled by default (`VERIFY_SSL = False`). Set to `True` if your API uses a valid SSL certificate.

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

## Output

- **analytics.json**: Summary of analytics in JSON format.
- **analytics.csv**: CSV report with metrics and car model counts.
- **car_popularity_metrics.png**: Bar chart showing car model popularity.

## Project Structure

- `main.py` - Entry point for running analytics.
- `api_client.py` - Handles API requests.
- `analytics.py` - Performs data analysis.
- `report_generator.py` - Generates reports (JSON, CSV, plots).
- `requirements.txt` - Python dependencies.

## Notes

- Make sure your API provides booking data at `/api/v1/bookings`.
- For a compatible API implementation, see: [vehicle-rental-management](https://github.com/ArjunSingh99/vehicle-rental-management)

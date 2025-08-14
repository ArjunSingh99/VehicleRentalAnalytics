import folium
import webbrowser
import tempfile
from datetime import datetime

class Tracking:
    def __init__(self, vehicle_data, map_centre=(0, 0)):
        self.vehicle_data = vehicle_data
        self.map_centre = map_centre

        self.zoom_start = 5

    def plot_vehicle_locations(self, output_file='vehicle_tracking_map.html', show_track=False):
        # Create a map centered around the average location
        track_map = folium.Map(location=self.map_centre, zoom_start=self.zoom_start)

        # Sort vehicle data by timestamp
        sorted_data = sorted(self.vehicle_data, key=lambda v: datetime.fromisoformat(v['timestamp']))

        # Add vehicle markers to the map
        for vehicle in sorted_data:
            lat = vehicle['latitude']
            lon = vehicle['longitude']
            time = datetime.fromisoformat(vehicle['timestamp'])
            folium.Marker(
                location=(lat, lon),
                popup=time.strftime('%Y-%m-%d %H:%M:%S'),
            ).add_to(track_map)

        # Add a polyline to show the track if requested
        track_coords = [(v['latitude'], v['longitude']) for v in sorted_data]
        if show_track and len(track_coords) > 1:
            folium.PolyLine(track_coords, color="blue", weight=3, opacity=0.7).add_to(track_map)

        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp_file:
            tmp_file_path = tmp_file.name
            track_map.save(tmp_file_path)

        webbrowser.open(f"file://{tmp_file_path}")
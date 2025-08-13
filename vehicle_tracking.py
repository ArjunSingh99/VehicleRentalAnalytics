import folium
import webbrowser
import tempfile

class Tracking:
    def __init__(self, vehicle_data, map_centre=(0, 0)):
        self.vehicle_data = vehicle_data
        self.map_centre = map_centre

        self.zoom_start = 5

    def plot_vehicle_locations(self, output_file='vehicle_tracking_map.html'):
        # Create a map centered around the average location
        track_map = folium.Map(location=self.map_centre, zoom_start=self.zoom_start)

        # Add vehicle markers to the map
        for vehicle in self.vehicle_data:
            lat = vehicle['latitude']
            lon = vehicle['longitude']
            folium.Marker(
                location=(lat, lon),
                popup="Booking ID",
            ).add_to(track_map)
        
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp_file:
            tmp_file_path = tmp_file.name
            track_map.save(tmp_file_path)

        webbrowser.open(f"file://{tmp_file_path}")
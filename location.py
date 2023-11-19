import geocoder
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

def get_location_by_coordinates(lat, lon):
    try:
        location = geolocator.reverse((lat, lon))
        return location.address
    except Exception as e:
        return str(e)

# Example coordinates


g = geocoder.ip('me')

# Latitude and Longitude
print(f"Latitude and Longitude: {g.latlng}")
latitude = g.latlng[0]
longitude = g.latlng[1]
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
address = get_location_by_coordinates(latitude, longitude)
print(f"Address: {address}")
# City
if g.city:
    print(f"City: {g.city}")
else:
    print("City information not available")

# Country
if g.country:
    print(f"Country: {g.country}")
else:
    print("Country information not available")

# State or Region
if g.state:
    print(f"State/Region: {g.state}")
else:
    print("State/Region information not available")

# Complete Address (if available)
if g.address:
    print(f"Address: {g.address}")
else:
    print("Address information not available")
import geocoder
import requests
import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

def get_location_by_coordinates(lat, lon):
    print(lat," ", lon)
    try:
        location = geolocator.reverse((lat, lon))
        return location.address
    except Exception as e:
        return str(e)

# Example coordinates




send_url = "http://api.ipstack.com/check?access_key=f97bdfdeb683f7b248409e58b68c97d0"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

# # Latitude and Longitude
# print(f"Latitude and Longitude: {g.latlng}")
# latitude = g.latlng[0]
# longitude = g.latlng[1]
print(f"Latitude: {latitude} Longitude: {longitude}")
address = get_location_by_coordinates(latitude, longitude)
print(f"Address: {address}")
# # City
# 22.51787658144267, 88.41656619016217
# if g.city:
#     print(f"City: {g.city}")
# else:
#     print("City information not available")

# # Country
# if g.country:
#     print(f"Country: {g.country}")
# else:
#     print("Country information not available")

# # State or Region
# if g.state:
#     print(f"State/Region: {g.state}")
# else:
#     print("State/Region information not available")

# # Complete Address (if available)
# if g.address:
#     print(f"Address: {g.address}")
# else:
#     print("Address information not available")

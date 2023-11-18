from plyer import gps

def get_location():
    try:
        gps.configure(on_location=on_location, on_status=on_status)
        gps.start(minTime=1000, minDistance=0)
    except Exception as e:
        print("An error occurred: " + str(e))

def on_location(**kwargs):
    print(f"Latitude: {kwargs['lat']}, Longitude: {kwargs['lon']}")

def on_status(stype, status):
    print(f"Status: {stype}, {status}")

# Call this function to start the GPS
get_location()

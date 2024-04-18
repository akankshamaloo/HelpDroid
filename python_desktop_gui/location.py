import requests

def get_location(ip_address):
    api_key = 'f93522e04e1ba3db108fee7552d4843352a9536215451b6a42e67b40'  # Replace with your actual API key from ipdata.co
    url = f'https://api.ipdata.co/{ip_address}?api-key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        data = response.json()
        return {
            'country_name': data.get('country_name'),
            'region': data.get('region'),
            'city': data.get('city'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude')
        }
    else:
        print( "Failed to retrieve data")
        return None



    


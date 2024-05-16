import requests

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    data = response.json()
    if data:
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])
        return {"latitude": latitude, "longitude": longitude}
    else:
        return None

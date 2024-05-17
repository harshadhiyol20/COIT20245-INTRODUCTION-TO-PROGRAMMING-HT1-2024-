import requests

def gps_coordinate(city):
    # url = "https://nominatim.openstreetmap.org/search?q=" + city + "&format=json"
    url = f"https://us1.locationiq.com/v1/search?key=pk.2d900a55b458c544056d8ae89a373738&q={city}&format=json"
    response = requests.get(url)
    data = response.json()
    # print(data)

    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return {"latitude": latitude, "longitude": longitude}
    else:
        return None

# def test_gps_coordinate():
#     coordinates = gps_coordinate("Brisbane")
#     assert coordinates == {'latitude': -27.4689682, 'longitude': 153.0234991}
#     print("Test passed for Brisbane")
#     print(coordinates)

# test_gps_coordinate()

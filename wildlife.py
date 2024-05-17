import requests

def get_species_list(coordiantes,radius):
    latitude = coordiantes['latitude']
    longitude = coordiantes['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={latitude},{longitude},{radius}"
    response = requests.get(url)
    data = response.json()
    
    # print(data)
    species_list = []
    for species in data['SpeciesSightingSummariesContainer']['SpeciesSightingSummary']:
        species_data = species['Species']
        species_list.append(species_data)

    # print(species_list)
    return species_list

# coordiante = { "latitude": -27.4689682, "longitude": 153.0234991 }
# get_species_list(coordiante, 10000)

def get_surveys_by_species(coordinate, radius, taxonid):
    latitude = coordinate['latitude']
    longitude = coordinate['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&&circle={latitude},{longitude},{radius}"
    response = requests.get(url)
    data = response.json()

    # print(data)
    survey = []
    if data["features"]:
        for species in data['features']:
            species_data = species['properties']
            survey.append(species_data)
    else:
        survey.append("List is Empty")

    # print(survey)
    # print(species_list)
    return survey

# coordiante = { "latitude": -27.4689682, "longitude": 153.0234991 }
# get_surveys_by_species(coordiante, 10000, 890)

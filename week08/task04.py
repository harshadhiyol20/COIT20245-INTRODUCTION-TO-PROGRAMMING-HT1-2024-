def search_sightings(taxonid, city):
    # Stub implementation, replace with actual web service call
    return [
        {"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_sightings(sightings):
    for sighting in sightings:
        print(f"Start Date: {sighting['properties']['StartDate']}, Locality Details: {sighting['properties']['LocalityDetails']}")


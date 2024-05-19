from nominatim import gps_coordinate
from wildlife import get_species_list, get_surveys_by_species
from datetime import datetime

# Task-1 
def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Animal species in a city - use 'species <city>' or 'species <city> venomous' commands")
    print("c. Animal Sighting in a city - enter the command in the format : 'sighting <city name> <Taxon ID>'")
    print("d. Exit")

# Task-3
def search_species(city):
    RADIUS = 100000
    coordiantes = gps(city)
    # print(coordiantes)
    species_list = get_species_list(coordiantes, RADIUS)
    return species_list

def display_species(species_list):
    print("\nDetail of species : \n")
    
    for entry in species_list:
        if "AcceptedCommonName" in entry:
            print(
                "TaxonID : " + str(entry["TaxonID"]) + "\n"
                "Name of the species : " + entry["AcceptedCommonName"] + "\n"
                "Pest Status : " + entry["PestStatus"] + "\n")
            print("--"*30+"\n")
        else:
            print(
                "TaxonID : " + str(entry["TaxonID"]) + "\n"
                "Scientific Name of the species : " + entry["ScientificName"] + "\n"
                "Pest Status : " + entry["PestStatus"] + "\n")
            print("--"*30+"\n")

# Task-4
def search_sightings(taxonid, city):
    # Stub implementation
    return [{ "properties": { "TaxonID":"860","StartDate":"1999-11-15","LocalityDetails":"Tinaroo","SiteCode":"INCIDENTAL" } }]


def display_sightings(sightings):
    print("\nAnimal sightings:")
    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        print(f"Animal was sighted in {locality} on {start_date}\n")

# Task-5
def filter_venomous(species_list):
    venomous_species = []
    for entry in species_list:
        if entry["PestStatus"] == "Venomous":
            venomous_species.append(entry)
    return venomous_species

# Task-6
def gps(city):
    return gps_coordinate(city)

# Task-2
def main():

    display_menu()

    while True:
        user_input = input("wildlife > ")

        if user_input.lower() == "help":
            display_menu()

        elif user_input.lower() == "exit":
            print("\nExiting the program.")
            break

        elif user_input.lower().startswith("species"):
            parts = user_input.split(" ")
            if len(parts) < 2:
                print("Invalid command format. Please use 'species <city>' or 'species <city> venomous'")
            else:
                city = parts[1]
                if len(parts) > 2 and parts[2].lower() == "venomous":
                    species_list = search_species(city)
                    venomous_species = filter_venomous(species_list)
                    
                    if venomous_species:
                        display_species(venomous_species)
                    else:
                        print("Venomous Species not found!")

                else:
                    species_list = search_species(city)
                    display_species(species_list)

        elif user_input.lower().startswith("sighting"):
            parts = user_input.split(" ")
            if len(parts) != 3:
                print("\nInvalid command format. Please enter the command in the format: sighting <city name> <Taxon ID>")
            else:
                _, city, taxonid = parts
                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
            
        else:
            print("Error: Invalid command")

if _name_ == "_main_":
    main()

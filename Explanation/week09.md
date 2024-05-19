 Week-9 | Explanation of all the tasks in week-9

 ## Task 6 | Add a GPS stub

 ### code :
 py
# Task-1 
def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Animal species in a city")
    print("c. Exit")

# Task-3 - updated function
def search_species(city):

    coordiantes = gps(city)
    test_gps(coordiantes)

    return [
        {"Species":{"TaxonID":1039,"AcceptedCommonName":"dolphin","PestStatus":"Nil"}},
        {"Species":{"TaxonID":1040,"AcceptedCommonName":"snake","PestStatus":"Venomous"}}
    ]

def display_species(species_list):

    print("\nDetail of species : \n")
    for species in species_list:
        print(
            "TaxonID : " + str(species["Species"]["TaxonID"]) + "\n"
            "Name of the species : " + species["Species"]["AcceptedCommonName"] + "\n"
            "Pest Status : " + species["Species"]["PestStatus"] + "\n")

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
    for species in species_list:
        if species["Species"]["PestStatus"] == "Venomous":
            venomous_species.append(species)
    return venomous_species

def test_filter_venomous(venomous_species):
    assert venomous_species == [{"Species":{"TaxonID":1040,"AcceptedCommonName":"snake","PestStatus":"Venomous"}}]
    return True

# Task-6 - newly added task
def gps(city):
    return { "latitude": -27.4689682, "longitude": 153.0234991 }

def test_gps(coordinates):
    assert coordinates == {"latitude": -27.4689682, "longitude": 153.0234991}
    return True

# Task-2
def main():
  
    display_menu()

    while True:
        user_input = input("wildlife > ")

        if user_input.lower() == "help":
            display_menu()
        elif user_input.lower() == "exit":
            print("Exiting the program.")
            break
            
        # Updated functionality according to the task
        elif user_input.lower().startswith("species"):
            parts = user_input.split(" ")
            if len(parts) < 2:
                print("Invalid command format. Please use 'species <city>' or 'species <city> venomous'")
            else:
                city = parts[1]
                if len(parts) > 2 and parts[2].lower() == "venomous":
                    species_list = search_species(city)
                    venomous_species = filter_venomous(species_list)
                    assert_value = test_filter_venomous(venomous_species)
                            
                    if assert_value:
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
            print("Error: Invalid command. Please enter 'help' or 'exit'.")


if _name_ == "_main_":
    main()


### output :

COIT20245 - Assignment 2

Menu :
a. Help Menu
b. Animal species in a city
c. Exit
wildlife > species cairns

Detail of species :

TaxonID : 1039
Name of the species : dolphin
Pest Status : Nil

TaxonID : 1040
Name of the species : snake  
Pest Status : Venomous       

wildlife >


### task-6 :Explanation
In this task we defined one function gps(city), which return the latitude and longitude. As this is also a stub that means it will provide the similar output which we already provided in code. 

In this task we define gps(city) and test_gps for the gps(city) has one parameter of city and test_gps(coordinate) has coordinate as one parameter which include latitude and longitude value. 

Then also need to update search_species function then it will able to call the gps(city). As the search_species is also a stub that's why it give the same output.


## Task-7 | GPS Webservice Module

### code :
py
# For this task we have created the nominatim file which gives us the coordinates of the city we give as an input
# you can see this file in the main branch

from nominatim import gps_coordinate

# Task-1 
def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Animal species in a city")
    print("c. Animal Sighting in a city")
    print("d. Exit")

# Task-3
def search_species(city):

    coordiantes = gps(city)

    return [
        {"Species":{"TaxonID":1039,"AcceptedCommonName":"dolphin","PestStatus":"Nil"}},
        {"Species":{"TaxonID":1040,"AcceptedCommonName":"snake","PestStatus":"Venomous"}}
    ]

def display_species(species_list):

    print("\nDetail of species : \n")
    for species in species_list:
        print(
            "TaxonID : " + str(species["Species"]["TaxonID"]) + "\n"
            "Name of the species : " + species["Species"]["AcceptedCommonName"] + "\n"
            "Pest Status : " + species["Species"]["PestStatus"] + "\n")

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
    for species in species_list:
        if species["Species"]["PestStatus"] == "Venomous":
            venomous_species.append(species)
    return venomous_species

def test_filter_venomous(venomous_species):
    assert venomous_species == [{"Species":{"TaxonID":1040,"AcceptedCommonName":"snake","PestStatus":"Venomous"}}]
    return True

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
            print("Exiting the program.")
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
                    assert_value = test_filter_venomous(venomous_species)
                    
                    if assert_value:
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


if __name__ == "__main__":
    main()


### output :

COIT20245 - Assignment 2

Menu :
a. Help Menu
b. Animal species in a city 
c. Animal Sighting in a city
d. Exit
wildlife >  gps_coordinate(city)
Error: Invalid command
wildlife > species cairns       

Detail of species : 

TaxonID : 1039
Name of the species : dolphin
Pest Status : Nil

TaxonID : 1040
Name of the species : snake
Pest Status : Venomous

wildlife >


## Task-7 explanation

In this we add one function gps_coordinate(city), which provide the coordinates in terms of latitude and longitude but on the same time we need to create one nominatim.py file in which the gps_coordinate(city) provide the data and send that data to the search species where it has gps(city) stub and we have to update it as well to call gps_coordinate(city).<br>

Also in nominatim we also fetch the url with which convert the response from JSON and convert longitude and latitude from string into floats.

## Task-8 | Wildlife Module Get Species List


### code :
py
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

if __name__ == "__main__":
    main()


### output :

TaxonID : 18541
Scientific Name of the species : Polyrhachis daemeli
Pest Status : Nil

------------------------------------------------------------

TaxonID : 18552
Name of the species : ghost ant
Pest Status : Feral Animal

------------------------------------------------------------

TaxonID : 18561
Scientific Name of the species : Tetramorium simillimum
Pest Status : Feral Animal

------------------------------------------------------------

TaxonID : 19621
Name of the species : honey bees
Pest Status : Nil

------------------------------------------------------------

TaxonID : 19224
Name of the species : white oak-blue
Pest Status : Nil

------------------------------------------------------------


### task8- explanation
for this task we need to make one python file as wildlife.py. Then we need to defined one function *get_species_list(coordinate,radius)* to recieve the list of the species in an area. The data fatch from the URL which provide data into JSON and then extract and return the species list and need to perform assert fuction and if test is successful then comment out. Then we need to import wildlife.py in sighting.py. After that need to update search_species(city) fuction becuause after that it is able to call get_species_list(coordinate, radius) function, in this function we defined the radius which is constant about 100000m which is equal to the 100 km becuase we need to search species within 100 km. After this need to add assert statement for further test of the search_species(city) function if works properly then need to comment out.

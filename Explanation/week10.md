Week-10 | Explanation of the tasks 9 and 10 in week-10


## Task-9 | Wildlife Module Get Surveys by Species


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
            print("--"*20+"\n")
        else:
            print(
                "TaxonID : " + str(entry["TaxonID"]) + "\n"
                "Scientific Name of the species : " + entry["ScientificName"] + "\n"
                "Pest Status : " + entry["PestStatus"] + "\n")
            print("--"*20+"\n")

# Task-4
def search_sightings(taxonid, city):
    RADIUS = 100000
    coordiantes = gps(city)

    surveys = get_surveys_by_species(coordiantes, RADIUS, taxonid)
    filtered_surveys = []
    for survey in surveys:
        if survey["SiteCode"] == "INCIDENTAL":
            filtered_surveys.append(survey)
    
    return filtered_surveys

def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    print("\nAnimal sightings:\n")
    for sighting in sorted_sightings:
        taxonid = sighting["TaxonID"]
        start_date = sighting["StartDate"]
        locality = sighting["LocalityDetails"]
        print(f"\nAnimal with TaxonID {taxonid} was sighted in {locality} on {start_date}\n")
        print("--"*60)

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

----------------------------------------

TaxonID : 18552
Name of the species : ghost ant
Pest Status : Feral Animal

----------------------------------------

TaxonID : 18561
Scientific Name of the species : Tetramorium simillimum
Pest Status : Feral Animal

----------------------------------------

TaxonID : 19621
Name of the species : honey bees
Pest Status : Nil

----------------------------------------

TaxonID : 19224
Name of the species : white oak-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19268
Name of the species : small dusky-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19269
Name of the species : twin dusky-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19263
Name of the species : shining pencilled-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19311
Name of the species : pale pea-blue
Pest Status : Nil

----------------------------------------

TaxonID : 20557
Scientific Name of the species : Danis sp.
Pest Status : Nil

----------------------------------------

TaxonID : 19325
Name of the species : spotted pea-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19320
Name of the species : orange-tipped pea-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19318
Name of the species : black-spotted grass-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19326
Name of the species : jewelled grass-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19211
Name of the species : copper jewel
Pest Status : Nil

----------------------------------------

TaxonID : 18
Name of the species : Apollo jewel (Wet Tropics subspecies)
Pest Status : Nil

----------------------------------------

TaxonID : 19
Name of the species : Apollo jewel (Torres Strait subspecies)
Pest Status : Nil

----------------------------------------

TaxonID : 19253
Name of the species : orchid flash
Pest Status : Nil

----------------------------------------

TaxonID : 19252
Name of the species : black-spotted flash
Pest Status : Nil

----------------------------------------

TaxonID : 19249
Name of the species : Macqueen's hairstreak
Pest Status : Nil

----------------------------------------

TaxonID : 19307
Name of the species : purple cerulean
Pest Status : Nil

----------------------------------------

TaxonID : 19314
Name of the species : plumbago blue
Pest Status : Nil

----------------------------------------

TaxonID : 19279
Name of the species : green-banded line-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19278
Name of the species : white-banded line-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19238
Name of the species : sapphire azure
Pest Status : Nil

----------------------------------------

TaxonID : 3
Name of the species : large moonbeam (Wet Tropics)
Pest Status : Nil

----------------------------------------

TaxonID : 21774
Scientific Name of the species : Philiris diana fortuna
Pest Status : Nil

----------------------------------------

TaxonID : 19222
Name of the species : blue moonbeam (Wet Tropics)
Pest Status : Nil

----------------------------------------

TaxonID : 19287
Name of the species : small green-banded blue
Pest Status : Nil

----------------------------------------

TaxonID : 19299
Name of the species : wattle blue (Cape York subspecies)
Pest Status : Nil

----------------------------------------

TaxonID : 19297
Name of the species : cycad blue (northern subspecies)
Pest Status : Nil

----------------------------------------

TaxonID : 2007
Name of the species : delicate blue
Pest Status : Nil

----------------------------------------

TaxonID : 19315
Name of the species : spotted grass-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19317
Name of the species : common grass-blue (Cape York subspecies)
Pest Status : Nil

----------------------------------------

TaxonID : 19316
Name of the species : common grass-blue (Australian subspecies)
Pest Status : Nil

----------------------------------------

TaxonID : 19319
Name of the species : dainty grass-blue
Pest Status : Nil

----------------------------------------

TaxonID : 19149
Name of the species : glasswing
Pest Status : Nil

----------------------------------------

TaxonID : 36145
Name of the species : tawny coster
Pest Status : Nil

----------------------------------------

TaxonID : 19150
Name of the species : red lacewing
Pest Status : Nil

----------------------------------------



### task-9 explanation
* We defined one function *get_surveys_by_species* in which there are three parameter *coordinate, **radius, and **taxonid*. by which we can get the animal survey data. <br>

Then after comment out the assert statement we need to update the search_sighting(taxonid,city) function because after that it is able to call the get_survey_by_species(coordinate, radius, taxonid) fuction,  and then need to filter out those functions which has sitecode as an identical those are acceptable






## Task- 10 

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
            print("--"*20+"\n")
        else:
            print(
                "TaxonID : " + str(entry["TaxonID"]) + "\n"
                "Scientific Name of the species : " + entry["ScientificName"] + "\n"
                "Pest Status : " + entry["PestStatus"] + "\n")
            print("--"*20+"\n")

# Task-4
def search_sightings(taxonid, city):
    RADIUS = 100000
    coordiantes = gps(city)

    surveys = get_surveys_by_species(coordiantes, RADIUS, taxonid)
    filtered_surveys = []
    for survey in surveys:
        if survey["SiteCode"] == "INCIDENTAL":
            filtered_surveys.append(survey)
    
    return filtered_surveys

def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    print("\nAnimal sightings:\n")
    for sighting in sorted_sightings:
        taxonid = sighting["TaxonID"]
        start_date = sighting["StartDate"]
        locality = sighting["LocalityDetails"]
        print(f"\nAnimal with TaxonID {taxonid} was sighted in {locality} on {start_date}\n")
        print("--"*60)

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

# Task-10
def earliest(sightings):
    return min(sightings, key=lambda x: x["StartDate"])

def sort_by_date(sightings):
    sorted_sightings = []
    while sightings:
        earliest_sighting = earliest(sightings)
        sorted_sightings.append(earliest_sighting)
        sightings.remove(earliest_sighting)
    return sorted_sightings

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


COIT20245 - Assignment 2

Menu :
a. Help Menu
b. Animal species in a city - use 'species <city>' or 'species <city> venomous' commands
c. Animal Sighting in a city - enter the command in the format : 'sighting <city name> <Taxon ID>'
d. Exit
wildlife > sighting cairns 860

Animal sightings:


Animal with TaxonID 860 was sighted in Ravenshoe Township on 1993-12-29

------------------------------------------------------------------------------------------------------------------------

Animal with TaxonID 860 was sighted in Tinaroo Dam, lake edge behind Tinaroo township on 1999-09-20

------------------------------------------------------------------------------------------------------------------------

Animal with TaxonID 860 was sighted in Tinaroo Lake edge - c. 1Km south of Tobacco Hill on 1999-11-15

------------------------------------------------------------------------------------------------------------------------

Animal with TaxonID 860 was sighted in Groves Creek, between Koah Road and Kennedy Highway, Koah on 2004-08-27

------------------------------------------------------------------------------------------------------------------------

Animal with TaxonID 860 was sighted in Tumoulin Rd, 8.5 km direct line NNW of Ravenshoe on 2020-07-13

------------------------------------------------------------------------------------------------------------------------
wildlife >



### week-10 Explanation

In this task we need to sort the animal sighting python file by the date as per the clent requirment and for that we need to create one function sort_by_date(sighting) which provide the details of sighting which are sorted by the date and also need to take in consider the function of function earliest().
Then need to update display_sighting() fuction which sorted by the date.

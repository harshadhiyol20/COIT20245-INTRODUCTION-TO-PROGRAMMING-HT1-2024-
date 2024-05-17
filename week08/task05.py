# Task-1 
def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Animal species in a city")
    print("c. Exit")

# Task-3
def search_species(city):
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

# Task-5 - new Added
def filter_venomous(species_list):
    venomous_species = []
    for species in species_list:
        if species["Species"]["PestStatus"] == "Venomous":
            venomous_species.append(species)
    return venomous_species

def test_filter_venomous(venomous_species):
    assert venomous_species == [{"Species":{"TaxonID":1040,"AcceptedCommonName":"snake","PestStatus":"Venomous"}}]
    return True

# Task-2 - Updated
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


if __name__ == "__main__":
    main()

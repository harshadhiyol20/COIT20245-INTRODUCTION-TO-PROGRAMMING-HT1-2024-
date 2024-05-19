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
            
            if len(parts) != 2:
                print("Error: Invalid command.")
            else :
                city = parts[1]
                species_list = search_species
        else:
            print("Error: Invalid command. Please enter 'help' or 'exit'.")


if _name_ == "_main_":
    main()

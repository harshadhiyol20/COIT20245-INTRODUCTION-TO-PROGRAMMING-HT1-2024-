 Week-8 | Explanation of all the tasks in week-8

## Task-1 | Display Menu

### Code : 
py
def display_menu():
    print("COIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Exit")

if __name__ == "__main__":
    display_menu()


### Output :

COIT20245 - Assignment 2

Menu : 
a. Help Menu
b. Exit


## Task-2 | User Input 

### code :
py
def main():

    display_menu()

    while True:
        user_input = input("wildlife > ")

        if user_input.lower() == "help":
            display_menu()
        elif user_input.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Error: Invalid command. Please enter 'help' or 'exit'.")


if __name__ == "__main__":
    main()


### output :

COIT20245 - Assignment 2

Menu :      
a. Help Menu
b. Exit
wildlife > help

COIT20245 - Assignment 2

Menu :
a. Help Menu
b. Exit
wildlife > exit
Exiting the program.

### Task-2 Explanation
For this task we defined *main* function, which display the menu. after that in wildlife > user need to provide the input as help or exit <br> </br>
In this user has two input values:
* (1) help : If user provide help as an input, it display the menu. 
* (2) exit : If user provide exit as an input, it display *exiting the program* and *exit* from the program.
 

## Task-3 | List Species in City (Stub)

### code :
py
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
                species_list = search_species(city)
                display_species(species_list)
        else:
            print("Error: Invalid command. Please enter 'help' or 'exit'.")


if __name__ == "__main__":
    main()


### output

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

### Task-3 Explanation 
* For this task user has to provide the input value. 
* In this user can use the *species cairns* and they will get the details of the species as an output.
* For this task we define two functions:<br> </br>
(1) search_species: Which is stub function right now which only returns the default values of species. We have provided values *taxonID, **AcceotedCommonName, and the **peststauts* for the two species.<br>
(2) display_species: Which display the details of the species list with above three parameter.



## Task-4 | List Animal Sightings in City (Stub)

### code :
py
# Task-1 
def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Animal species in a city")
    print("c. Animal sighting in a city")
    print("d. Exit")

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

# Task-4 - requirements
def search_sightings(taxonid, city):
    # Stub implementation
    return [{ "properties": { "TaxonID":"860","StartDate":"1999-11-15","LocalityDetails":"Tinaroo","SiteCode":"INCIDENTAL" } }]


def display_sightings(sightings):
    print("\nAnimal sightings:")
    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        print(f"Animal was sighted in {locality} on {start_date}\n")

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
        elif user_input.lower().startswith("species"):
            parts = user_input.split(" ")
            
            if len(parts) != 2:
                print("Error: Invalid command.")
            else :
                city = parts[1]
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


### output :

COIT20245 - Assignment 2

Menu :
a. Help Menu
b. Animal species in a city
c. Animal sighting in a city
d. Exit
wildlife > sightings Cairns 1039

Animal sightings:
Animal was sighted in Tinaroo on 1999-11-15

wildlife >



### Task-4 Explanation
* In this task user need provide input  *sightings Cairns 1039*.
* For this task we define one function *search_sightings* which has two variable *taxonid* and *city. And it return the following properties such as **TaxonID, **starDate, **LocalityDetails* and its *SiteCode*. This function again is stub implementation which returns default value that we have provided.
 

## Task-5 | List Venomous Animal Sightings in a City
### code :

py
# Task-1 
def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Animal species in a city")
    print("c. Animal sighting in a city")
    print("d. Exit")

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


if _name_ == "_main_":
    main()


### output :

COIT20245 - Assignment 2

Menu :
a. Help Menu
b. Animal species in a city
c. Animal sighting in a city
d. Exit
wildlife > species cairns venomous

Detail of species : 

TaxonID : 1040
Name of the species : snake
Pest Status : Venomous

wildlife >


### Task-5 Explanation
For this task we defiened *filter_venomous(species_list)* function, through this we can get the details of the only of those which has PestStatus as Venomous.
*test_filter_venomous* is also defined with *venomous_species* variable, which is an asserts (testing function) takes an argument *venomous_species* with *TaxonID, **AccepredCommonName, and **PestStatus. Then return the True if list have any species with **PestStatus = Venomous*.
* For this user has to provide the input *species Cairns venomous*. <br> </br>

This is how we did the week 8 by understanding the requirement and develope a code according the demand.

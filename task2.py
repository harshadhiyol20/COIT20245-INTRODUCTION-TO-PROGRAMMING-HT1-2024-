def main():
  
    display_menu()

    while True:
        user_input = input("wildlife > ")

        if user_input.lower() == "help":
            display_menu()
        elif user_input.lower() == "exit":
            print("Exiting the program.")
            break
        elif user_input.lower() == "species":
            city = input("Enter the city: ")
            species_list = search_species(city)
            display_species(species_list)
        else:
            print("Error: Invalid command. Please enter 'help' or 'exit'.")




def main():
    display_menu()
    while True:
        command = input("wildlife> ")
        if command.lower() == "help":
            display_menu()
        elif command.lower() == "exit":
            break
        elif command.lower().startswith("species"):
            city = command.split()[1]
            species_list = search_species(city)
            display_species(species_list)
        elif command.lower().startswith("sightings"):
            parts = command.split()
            if len(parts) >= 3:
                taxonid = parts[1]
                city = parts[2]
                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
            else:
                print("Invalid command. Usage: sightings <taxonid> <city>")
        else:
            print("Invalid command. Please try again.")

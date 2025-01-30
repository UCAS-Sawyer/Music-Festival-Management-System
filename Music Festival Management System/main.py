#Music Festival Management System, Sawyer Wood, Alishya Xavier, Evan McCabe

Artists = []
schedule = []

#Venue list:
venues = []

def ArtistManagement(Artists):

    #Exceptions for floats
    def floatchecker(Inputx):
        try:
            Inputx = float(Inputx)
            return(Inputx)
        except:
            print("\nThat is not a valid input.")
            return False

    def AddArtist(Artists):
        #Getting Nescasary Inputs
        name = input("\nWhat is the name of the artist: \t")
        genre = input("\nWhat is the genre of the artist:\t")
        duration = floatchecker(input("\nWhat is the duration of the performance in hours:\t"))
        if duration != False:

            ArtistToBeAdded = {
                "Name" : name,
                "Genre" : genre,
                "Duration" : duration
            }

            #Adding it to the Artists list
            Artists.append(ArtistToBeAdded)
            print(f"\nThe artist {ArtistToBeAdded} has been added to the list.")

    def EditArtist(Artists):
        #Inputs
        name = input("\nWhat is the name of the artist that you want to edit: \t")
        #If the artist exists
        for x in Artists:
            if x["Name"] == name:
                print("\n", x)
                choice = input("\nWhat do you want to change, 1: Name, 2: Genre, 3: Duration :\t")

                if choice == "1":
                    x["Name"] = input("\nEnter the new name: \t")
                    print(f"\nThe new data is, {x}")
                    mainforArtistManagement()
                    return
                elif choice == "2":
                    x["Genre"] = input("\nEnter the new genre: \t")
                    print(f"\nThe new data is, {x}")
                    mainforArtistManagement()
                    return
                elif choice == "3":
                    x["Duration"] = input("\nEnter the new duration: \t")
                    print(f"\nThe new data is, {x}")
                    mainforArtistManagement()
                    return
                else:
                    print("\nThat is not a valid input.")
                    mainforArtistManagement()
                    return

        #If the artist does not exists    
        print(f"\nArtist {name} does not exist.")
        mainforArtistManagement()

    def RemoveArtist(Artists):
        #Inputs
        name = input("\nWhat is the name of the artist you would like to remove:\t")
        for x in Artists:
            if x["Name"] == name:
                Artists.remove(x)
                print(f"\nThe artist {name} has been removed.")
                mainforArtistManagement()
        print("\nAn atrist of that name does not exist.")
    
    def ViewArtists(Artists):
        print(f"\nAll of the artists are {Artists}")
        mainforArtistManagement()

    def mainforArtistManagement():
        choice = input("\nChoose what you want to do, 1: Add Artist, 2: Edit Artist, 3: Remove Artist, 4: View All Artists, 5: Quit : \t")
        if choice == "1":
            AddArtist(Artists)
        elif choice == "2":
            EditArtist(Artists)
        elif choice == "3":
            RemoveArtist(Artists)
        elif choice == "4":
            ViewArtists(Artists)
        elif choice == "5":
            main()
        else:
            print("\nInvalid choice.")
            mainforArtistManagement()

    while True:
        mainforArtistManagement()

###TicketSales Function
def TicketSalesAndAttendee(venues):

    #Exceptions for ints
    def intchecker(Inputx):
        try:
            Inputx = int(Inputx)
            return(Inputx)
        except:
            print("\nThat is not a valid input.")
            return False

    FestivalName = input("\nWhat is the name of the festival: \t")

    #For each festival in Festivals
    for x in venues:
        #If the festival exists
        if x["name"] == FestivalName:
            NumOfTickets = intchecker(input("\nHow many tickets are you inputting: \t"))
            if NumOfTickets != False:
                #For each ticket
                for y in range(NumOfTickets):
                    TicketType = input("\nWhat is the type of ticket you are entering, 1: 1-day, 2: 3-day, 3: VIP :\t")

                    #Which type of ticket is it?
                    if TicketType == "1":
                        Name = input("\nWhat is the name of the person: \t")
                        Person = {
                            "Person Name" : Name,
                            "Ticket Type" : "1-day"
                        }
                        x["Attendees"].append(Person)
                        print(f"\nAttendee {Person} has been added.")

                    elif TicketType == "2":
                        Name = input("\nWhat is the name of the person: \t")
                        Person = {
                            "Person Name" : Name,
                            "Ticket Type" : "3-day"
                        }
                        x["Attendees"].append(Person)
                        print(f"\nAttendee {Person} has been added.")

                    elif TicketType == "3":
                        Name = input("\nWhat is the name of the person: \t")
                        Person = {
                            "Person Name" : Name,
                            "Ticket Type" : "VIP"
                        }
                        x["Attendees"].append(Person)
                        print(f"\nAttendee {Person} has been added.")

                    else:
                        print("\nthat is not a valid input.")
        #If the festival does not exist
        else:
            print(f"\nFestival {FestivalName} does not exist.")
            main()

###Schedule management
def schedule_management(schedule):

    def remove_artist():
        remove_artist_name = input("What is the artist's name you want to remove: ")
        remove_artist_stage = input(f"What stage do you want to remove {remove_artist_name} from (example: 1): ")
        remove_artist_time = input(f"What time slot do you want to remove {remove_artist_name} from (example: 9:30 a.m. ): ")

        remove_entry = (remove_artist_name, remove_artist_time, remove_artist_stage)
        if remove_entry in schedule:
            schedule.remove(remove_entry)
            print("\nArtist removed from the schedule.\n")
        else:
            print("\nThat is not currently scheduled.\n")



    def add_artist():
        add_artist_name = input("What is the artist's name you want to add: ")
        add_artist_stage = input(f"What stage do you want to add {add_artist_name} to (example: 1): ")
        add_artist_time = input(f"What time slot do you want to add {add_artist_name} to (example: 9:30 a.m. ): ")

        new_entry = (add_artist_name, add_artist_time, add_artist_stage)
        if any(entry for entry in schedule if entry[1] == add_artist_time and entry[2] == add_artist_stage):
            print("\nThat spot is already assigned.\n")
        else:
            schedule.append(new_entry)
            print("\nArtist added to the schedule.\n")



    def display_schedule():
        if not schedule:
            print("\nThe schedule is currently empty.\n")
        else:
            print("\nCurrent schedule:")
            for entry in schedule:
                print(f"\nArtist: {entry[0]}, Time slot: {entry[1]}, Stage: {entry[2]}\n")



    def schedule_management_changes():
        while True:
            option = input('What do you want to change:\n1. Remove an artist from a time slot and stage\n2. Add an artist from a time slot and stage\n3. View the schedule\n4. Exit\n')
            if option == '1':
                remove_artist()
            elif option == '2':
                add_artist()
            elif option == '3':
                display_schedule()
            elif option == '4':
                break
            else:
                print('That is not an option')
                continue

    # Call the function to manage the schedule
    schedule_management_changes()

#Venue Management Function:
def venueManagement(venues):
    
	#Ask the user if they want to print all venues, add a venue, edit a venue, or remove a venue:
    choice = input("\nWhat would you like to do?\n1 = print all venues\n2 = add a venue\n3 = edit a venue\n4 = remove a venue\n5 = exit\n")

	#If the user chose print all venues:
    if choice == "1":
		#Print all venues on the list:
        for i in venues:
            for key, value in i.items():
                print(f"{key}: {value}")
            print("")

	#If the user chose add a venue:
    elif choice == "2":

		#Ask the user what the name of the venue is:
        name = input("\nWhat is the name of the venue?\n")

		#Ask the user for the location of the venue:
        location = input("\nWhere is the venue located?\n")

		#Ask the user for the equipment needed for the venue:
        equipment = input("\nWhat equipment is required for the venue?\n")

		#Add the venue to the list as specified by the user:
        venue = {
            "name": name,
            "location": location,
            "equipment": equipment ,
            "Attendees" : []
        }
        venues.append(venue)

        #Tell the user the venue was added successfully:
        print("\nVenue added.")

	
	#If the user chose edit a venue:
    elif choice == "3":

		#Ask the user which venue they want to edit:
        venue = input("\nWhat is the name of the venue you would like to edit?\n")

        #Check to make sure the user inputted a venue that exists:
        existant = False
        for i in venues:
            if i["name"] == venue:
                existant = True
        if existant == False:
            print("\nThat venue is not in the list, sorry. :/")
            venueManagement()

		#Ask the user what they want to change about the venue:
        change = input("\nWhat would you like to change about the venue?\n1 = name\n2 = location\n3 = equipment\n")

        #If the user chose to change the venue's name:
        if change == "1":

            #Ask the user what they want to change the venue's name to:
            newName = input("\nWhat would you like the name of the venue to be?\n")

            #Change the name of the venue as specified by the user:
            for i in venues:
                if i["name"] == venue:
                    i.update({"name": newName})

            #Tell the user the change was successful:
            print("\nName successfully changed.")

        #If the user chose to change the venue's location:
        elif change == "2":

            #Ask the user what they want to change the venue's location to:
            newLocation = input("\nWhat would you like the venue's location to be?\n")

            #Change the location of the venue as specified by the user:
            for i in venues:
                if i["name"] == venue:
                    i.update({"location": newLocation})

            #Tell the user the change was successful:
            print("\nLocation successfully changed.")

        #If the user chose to change the venue's equipment:
        elif change == "3":

            #Ask the user what they want to change the venue's equipment to:
            newEquipment = input("\nWhat would you like the venue's equipment to be changed to?\n")

            #Change the equipment of the venue as specified by the user:
            for i in venues:
                if i["name"] == venue:
                    i.update({"equipment": newEquipment})

            #Tell the user the change was successful:
            print("\nEquipment successfully changed.")

        #If the user did not choose a valid option:
        else:
            #Tell the user they chose an invalid option:
            print("\nThat isn't an option; please try again.")
            venueManagement()

	#If the user chose remove a venue:
    elif choice == "4":

		#Ask the user what venue they want to remove:
        byeByeVenue = input("\nWhat is the name of the venue you would like to remove?\n")

		#Remove venue from list as specified by the user:
        removed = False
        for i in venues:
            if i["name"] == byeByeVenue:
                venues.remove(i)
                removed = True

        #Tell the user if the venue was successfully removed:
        if removed == False:
            print("\nThat venue isn't on the list. :/")
        else:
            print("\nVenue successfuly removed.")

    #If the user chose to exit:
    elif choice == "5":

        pass

    #If the user didn't choose a valid option:
    else:
        #Tell the user they've made a mistake:
        print("\nINVALID INPUT\n\nPlease try again.")
        #Run the function again:
        venueManagement()


#Main Function:
def main():

	#Ask the user what function they want to perform:
    choice = input("\nWhat would you like to do?\n1 = manage artists\n2 = manage schedule\n3 = manage venues\n4 = ticket sales/attendee management\n5 = search\n6 = exit\n")

#If the user chose manage artists:
    if choice == "1":

	#Artist Management function call:
        ArtistManagement(Artists)

#If the user chose manage schedule:
    elif choice == "2":

	#Schedule Management function call:
        schedule_management(schedule)


#If the user chose manage venues:
    elif choice == "3":

	#Venue Management function call:
        venueManagement(venues)

#If the user chose ticket sales/attendee management:
    elif choice == "4":

	#Ticket Sales and Attendee Management function call:
        TicketSalesAndAttendee(venues)

#If the user chose search:
    elif choice == "5":

	#Search function call:
        search()

#If the user chose exit:
    elif choice == "6":
        print("\nExiting program.")
        raise SystemExit
        

#If the user chooses an invalid option:
    else:
        print("\nINVALID OPTION\n\nPlease try again. :/")

    main()

#Clearing Screen
print("\033[H\033[J")

main()

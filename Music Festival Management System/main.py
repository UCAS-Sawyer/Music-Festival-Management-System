#Music Festival Management System, Sawyer Wood, Alishya Xavier, Evan McCabe

Artists = []
schedule = []

#Venue list:
venues = []

#Artist Management Made by: Sawyer
def ArtistManagement(Artists, schedule, venues):

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
            main(Artists, schedule, venues)
        else:
            print("\nInvalid choice.")
            mainforArtistManagement()

    while True:
        mainforArtistManagement()

###TicketSales Function Made by: Sawyer
def TicketSalesAndAttendee(Artists, schedule, venues):

    #Exceptions for ints
    def intchecker(Inputx):
        try:
            Inputx = int(Inputx)
            return(Inputx)
        except:
            print("\nThat is not a valid input.")
            return False

    FestivalName = input("\nWhat is the name of the venue: \t")

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
            print(f"\nVenue {FestivalName} does not exist.")
            main(Artists, schedule, venues)

#This helps check if the time is right throughout the code
import re

#Schedule management function Made By: Alishya
def schedule_management(Artists, schedule, venues):

    def validate_time_slot(time_slot):
        # Format found online for how to make sure the time is written correctly
        pattern = re.compile(r'^(1[0-2]|[1-9]):[0-5][0-9] (a|p)\.m\.$')
        if pattern.match(time_slot):
            return True
        else:
            print("You didn't type in the time in the right way. Next time write it like 'hours:minutes a.m. or p.m.'")
            return False
        
    #This function removes an artist from schedule
    def remove_artist():
        if len(schedule) == 0:
            print('\nYou can\'t remove anything from the schedule because there isn\'t anything already booked\n')
        
        # This helps check if the stage is an int or if the time is written properly
        else:
            remove_artist_name = input("What is the artist's name you want to remove: ")
            remove_artist_stage = input(f"What stage do you want to remove {remove_artist_name} from (example: 1): ")
            try:
                remove_artist_stage = int(remove_artist_stage)
                remove_artist_time = input(f"What time slot do you want to remove {remove_artist_name} from (example: 9:30 a.m. ): ")
                if validate_time_slot(remove_artist_time):
                    remove_entry = (remove_artist_name, remove_artist_time, remove_artist_stage)
                    if remove_entry in schedule:
                        schedule.remove(remove_entry)
                        print("\nArtist removed from the schedule.\n")
                    else:
                        print("\nThat is not currently scheduled.\n")
            except ValueError:
                print('\nThat is not a valid stage number.\n')
                
    #This is the function to add an artist
    def add_artist():
        add_artist_name = input("What is the artist's name you want to add: ")
        add_artist_stage = input(f"What stage do you want to add {add_artist_name} to (example: 1): ")
        #This checks if the stage and time slot is written correctly in the right form
        try:
            add_artist_stage = int(add_artist_stage)
            add_artist_time = input(f"What time slot do you want to add {add_artist_name} to (example: 9:30 a.m. ): ")
            if validate_time_slot(add_artist_time):
                new_entry = (add_artist_name, add_artist_time, add_artist_stage)
                if any(entry for entry in schedule if entry[1] == add_artist_time and entry[2] == add_artist_stage):
                    print("\nThat spot is already assigned.\n")
                else:
                    schedule.append(new_entry)
                    print("\nArtist added to the schedule.\n")
        except ValueError:
            print('That is not a valid stage number.')

    #This function displays the schedule
    def display_schedule():
        if not schedule:
            print("\nThe schedule is currently empty.\n")
        else:
            print("\nCurrent schedule:")
            for entry in schedule:
                print(f"\nArtist: {entry[0]}, Time slot: {entry[1]}, Stage: {entry[2]}\n")

    #This function shows the user interface by asking them to pick what they want to do
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

    #This is called after the schedule management function is called
    schedule_management_changes()

#Venue Management Function Made By: Evan
def venueManagement(Artists, schedule, venues):
    
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
            venueManagement(venues)

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
        venueManagement(Artists, schedule, venues)

#Search Function By Evan:
def search(Artists, schedule, venues):

	#Ask the user if they want to search for an artist, a venue, or a ticket:
    choice = input("\nWhat would you like to search for?\n1 = artist\n2 = venue\n3 = ticket\n4 = exit\n")

	#If the user chose to search for an artist:
    if choice == "1":
		
		#Ask the user what artist they want to search for:
        artistName = input("\nWhat is the name of the artist you want to search for?\n")

		#Check if the artist the user wants to search for is on the list:
        exists = False
        for i in Artists:
            if i["Name"] == artistName:
                exists = True

		#Tell the user if the artist they want to search for is or isn’t on the list:
        if exists == True:
            print("\nThat artist is part of the festival.")
        else:
            print("\nThat artist is NOT part of the festival.")

	#If the user chose to search for a venue:
    elif choice == "2":

		#Ask the user what venue they would like to search for:
        venueName = input("What is the name of the venue you want to search for?\n")

		#Check if the venue the user wants to search for is on the list:
        exists = False
        for i in venues:
            if i["name"] == venueName:
                exists = True

		#Tell the user if the venue they want to search for is or isn’t on the list:
        if exists == True:
            print("\nThat venue is part of the festival.")
        else:
            print("\nThat venue is NOT part of the festival.")

	#If the user chose to search for a ticket:
    elif choice == "3":

		#Ask the user who they want to check has a ticket:
        ticketName = input("\nWhat is the name of the person you you would like to check has a ticket?\n")

		#Check if the person the user wants to check has a ticket:
        existant = False
        for x in venues:
            for y in x["Attendees"]:
                if y["Person Name"] == ticketName:
                    existant = True

		#Tell the user if the person the user wants to check does or does not have a ticket:
        if exists == True:
            print("\nThat person has bought a ticket.")
        else:
            print("\nThat person has NOT bought a ticket.")

    #If the user chose to exit:
    elif choice == "4":
        pass

    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        search(Artists, venues)

#Main Function Made By: Evan
def main(Artists, schedule, venues):

	#Ask the user what function they want to perform:
    choice = input("\nWhat would you like to do?\n1 = manage artists\n2 = manage schedule\n3 = manage venues\n4 = ticket sales/attendee management\n5 = search\n6 = exit\n")

#If the user chose manage artists:
    if choice == "1":

	#Artist Management function call:
        ArtistManagement(Artists, schedule, venues)

#If the user chose manage schedule:
    elif choice == "2":

	#Schedule Management function call:
        schedule_management(Artists, schedule, venues)

#If the user chose manage venues:
    elif choice == "3":

	#Venue Management function call:
        venueManagement(Artists, schedule, venues)

#If the user chose ticket sales/attendee management:
    elif choice == "4":

	#Ticket Sales and Attendee Management function call:
        TicketSalesAndAttendee(Artists, schedule, venues)

#If the user chose search:
    elif choice == "5":

	#Search function call:
        search(Artists, schedule, venues)

#If the user chose exit:
    elif choice == "6":
        print("\nExiting program.")
        raise SystemExit
        

#If the user chooses an invalid option:
    else:
        print("\nINVALID OPTION\n\nPlease try again. :/")

    main(Artists, schedule, venues)

#Clearing Screen
print("\033[H\033[J")

print("Welcome to the Music Festival Management!")
main(Artists, schedule, venues)
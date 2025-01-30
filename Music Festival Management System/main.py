#Music Festival Management System, Sawyer Wood, Alishya Xavier, Evan McCabe

Artists = []
schedule = []


#Example Festival
Festivals = [{
    "Festival Name" : "Kuthulu Festival Of Winter Solstice By Squiddles", 
    "Attendees": []
    }]

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
                elif choice == "2":
                    x["Genre"] = input("\nEnter the new genre: \t")
                    print(f"\nThe new data is, {x}")
                    mainforArtistManagement()
                elif choice == "3":
                    ################################################################################################################# Ask how to check if it will work
                    x["Duration"] = input("\nEnter the new duration: \t")
                    print(f"\nThe new data is, {x}")
                    mainforArtistManagement()
                else:
                    print("\nThat is not a valid input.")
                    mainforArtistManagement()

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
                mainforArtistManagement
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
            main(Artists)
        else:
            print("\nInvalid choice.")
            mainforArtistManagement()

    while True:
        mainforArtistManagement()

###TicketSales Function
def TicketSalesAndAttendee(Festivals):

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
    for x in Festivals:
        #If the festival exists
        if x["Festival Name"] == FestivalName:
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

#Clearing Screen
print("\033[H\033[J")

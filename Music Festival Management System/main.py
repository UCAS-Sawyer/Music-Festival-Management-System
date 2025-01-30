#Music Festival Management System, Sawyer Wood, Alishya Xavier, Evan McCabe

Artists = []

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

#Clearing Screen
print("\033[H\033[J")

ArtistManagement(Artists)

#Example Festival
Festivals = [{
    "Festival Name" : "Kuthulu Festival Of Winter Solstice By Squiddles", 
    "Attendees": []
    }]

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

#Clearing Screen
print("\033[H\033[J")


TicketSalesAndAttendee(Festivals)

#Music Festival Management System, Sawyer Wood, Alishya Xavier, Evan McCabe

#Example Festival
Festivals = [{
    "Festival Name" : "Sun", 
    "Attendees": []
    }]

def TicketSalesAdnAttendee(Festivals):

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

TicketSalesAdnAttendee(Festivals)
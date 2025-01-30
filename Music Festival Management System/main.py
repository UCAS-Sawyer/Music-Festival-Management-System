#Music Festival Management System, Sawyer Wood, Alishya Xavier, Evan McCabe

#Search Function:
def search(Artists, venues):

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
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
            return None

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
        name = input("\nWhat is the name of the artist that you want to edit: \t")

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
print("\nWelcome to the Personal Library Program(PLP)")

ArtistManagement(Artists)
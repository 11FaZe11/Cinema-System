import sys, time, pickle

def open_file(file_name, mode):

    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def password(user_password):

    password = "faze._11"
    if user_password == password:
        print("\nYour password was correct.\n access granted. \n ")
        return 1
    else:
        return None
        
def customer():

    choice = None
    while choice != "0":
        
        print(
        """
\t\tWelcome, Customer.


Please enter one of the options below and please make sure not to enter wrong input.
\U0001f600 \U0001f600 \U0001f600 \U0001f600

0 - Exit
1 - View Films
2 - View Ticket Prices
3 - Reserve Tickets
"""
            )

        choice = input("Choice: ")
        print()

        # this one is for exit      faze._11
        if choice == "0":
            print("Exiting menu...\n")

        # this one is for viewing films     faze._11
        elif choice == "1":
            try:
                file = open_file("films.dat", "rb")
                films = pickle.load(file)

                print("\nFilms Currently Showing:\n".upper())
                for key in sorted(films.keys()):
                    print(key)
                                  
                file.close()
            except EOFError:
                print("File is empty.")
                        

            input("\nPress the enter key to continue.")

        # this one is for viewing ticket prices     faze._11
        elif choice == "2":
            file = open_file("prices.dat", "rb")
            prices = pickle.load(file)
            adultPrice = prices["Adult"]
            childPrice = prices["Child"]
            concessionPrice = prices["Concession"]
            print("Current ticket prices are:\n",
                  "\nAdult: L.E", "%.2f" % adultPrice,
                  "\nChild: L.E", "%.2f" % childPrice,
                  "\nConcession: L.E", "%.2f" % concessionPrice)
            file.close()

            input("\nPress the enter key to continue.\n")

        # this one is for reserving tickets     faze._11
        elif choice == "3":
            try:
                file = open_file("showings.dat", "rb")
                showings = pickle.load(file)

                print("\nFilms Currently Showing:\n".upper())
                for key, value in sorted(showings.items()):
                    print(key)
                    print("Screen:  ", "Date:  ", "           Time:  ")
                    for highlist in value:
                        for lowlistitem in highlist:
                            print(lowlistitem, end="         ")
                        print("\n")
                print("\n")
                                     
                file.close()
            except EOFError:
                print("File is empty.")

            input("\nPress the enter key to continue.")
            print("\n")

            print("\n\nFill in the following information for the showing you wish to reserve.")
            filmToReserve = str(input("\nEnter the film title: "))
            dateToReserve = str(input("Enter the showing date, DD/MM/YYYY: "))
            timeToReserve = str(input("Enter the showing time, HH:MM : "))

            showingToReserve = [filmToReserve,dateToReserve,timeToReserve]

            numAdult = int(input("\nHow many adult tickets?: "))
            numChild = int(input("How many child tickets?: "))
            numConcession = int(input("How many concession tickets?: "))

            file = open_file("prices.dat", "rb")
            prices = pickle.load(file)

            adultPrice = prices["Adult"]
            childPrice = prices["Child"]
            concessionPrice = prices["Concession"]

            file.close()

            totalCost = (numAdult*adultPrice)+(numChild*childPrice)+(numConcession*concessionPrice)

            try:
                file = open_file("tickets_sold.dat", "rb")
                tickets_sold = pickle.load(file)
                adult_sold = tickets_sold["AdultSold"]
                child_sold = tickets_sold["ChildSold"]
                concession_sold = tickets_sold["ConcessionSold"]
                total_taken = tickets_sold["TotalTaken"]
                file.close()
            except EOFError:
                tickets_sold = {}
                adult_sold = 0
                child_sold = 0
                concession_sold = 0
                total_taken = 0                
                
            adult_sold += numAdult
            child_sold += numChild
            concession_sold += numConcession
            total_taken += totalCost

            file = open_file("tickets_sold.dat", "wb")
            tickets_sold["AdultSold"] = adult_sold
            tickets_sold["ChildSold"] = child_sold
            tickets_sold["ConcessionSold"] = concession_sold
            tickets_sold["TotalTaken"] = total_taken
            pickle.dump(tickets_sold, file)
            file.close()

            print("\nYour reservation has been received and is as follows:\n",
                  "\nFilm: ", filmToReserve, "on", dateToReserve, "at", timeToReserve,
                  "\nNumber of Adult tickets:", numAdult,
                  "\nNumber of Child tickets:", numChild,
                  "\nNumber of Concession tickets: ", numConcession,
                  "\n\nThe total to pay is: L.E", "%.2f" % totalCost)

            input("\nPress the enter key to continue.")
            print("\n")
            
        # if the user is an idoit lolzz    faze._11
        else:
            print("Sorry, but '", choice, "' isn't a valid choice.\n")

def manager():
    # this one is for the manager  faze._11
    choice = None
    while choice != "0":
        
        print(
        """
\t\tWelcome, Manager this system is all yours now you can do every thing for the 
following commands and please dont be an idiot like the stupid custmers.

Please enter one of the options below.

0 - Exit
1 - Set Ticket Prices
2 - Add/Remove Film
3 - Add/Remove Screen
4 - Add/Remove shows
5 - View Tickets Sold & Income
6 - Joke of the day \U0001F923
"""
            )

        choice = input("Choice: ")
        print()

        # this one is for exiting         faze._11
        if choice == "0":
            print("Wait......")
        #this one is for setting ticket prices      faze._11
        elif choice == "1":
            try:
                file = open_file("prices.dat", "rb")
                prices = pickle.load(file)
                print("Current ticket prices are:\n",
                      "\nAdult: L.E", prices["Adult"],
                      "\nChild: L.E", prices["Child"],
                      "\nConcession: L.E", prices["Concession"])
                file.close()
            except EOFError:
                print("File is empty. Set ticket prices for first time.")
                prices = {}
            

            change_prices = input("\nWould you like to change prices? yes/no: ")
            
            if change_prices == "yes":
                file = open_file("prices.dat", "wb")
                prices["Adult"] = float(input("\nAdult: L.E"))
                prices["Child"] = float(input("Child: L.E"))
                prices["Concession"] = float(input("Concession: L.E"))
                pickle.dump(prices, file)
                file.close()
            elif change_prices == "no":
                print("Sure... On your demand")
            else:
                print(change_prices, "is not recognised. Try again.")

            input("\nPress the enter key to continue.\n")
            
        # this on is for adding/removing films
        elif choice == "2":
            choice = None
            while choice != "0":
                # الحته دي عظمه       lolzzz           faze._11
                print(
        """
What would you like to do?

0 - Exit
1 - View Films
2 - Add Film
3 - Remove Film
"""
                )

                choice = input("Choice: ")
                print()

                # this one is for exiting    faze._11
                if choice == "0":
                    print("Wait/../")

                # this one is for viewing films     faze._11
                elif choice == "1":
                    try:
                        file = open_file("films.dat", "rb")
                        films = pickle.load(file)

                        print("\nFilms Currently Showing:\n".upper())
                        for key in sorted(films.keys()):
                            print(key)
                                  
                        file.close()
                    except EOFError:
                        print("File is empty.")

                    input("\nPress the enter key to continue.")
                    print("\n")
                        
                #this one is for adding a film      faze._11
                elif choice == "2":
                    while True:
                        Title = input("\nEnter the film title:                  OBLIGRATORY  ")
                        Description = input("Enter a description:                  OPTOINAL  ")
                        Age_rating = input("Enter the age rating:               OBLIGRATORY  ")
                        Star_rating = input("Enter a star rating:                  OPTOINAL  ")
                        Running_time = input("Enter the running time:           OBLIGRATORY  ")
                        Dimension = input("Is the film 2D or 3D?:                  OPTOINAL  ")
                        try:
                            file = open_file("films.dat", "rb")
                            films = pickle.load(file)
                            file.close()
                        except EOFError:
                            films = {}


                        details = (Description,
                                   "\nAge Rating: ", Age_rating,
                                   "Star Rating: ", Star_rating,
                                   "Running Time: ", Running_time,
                                   Dimension, "\n")
                    
                        films[Title] = details
                    
                    
                        file = open_file("films.dat", "wb")
                        pickle.dump(films, file)
                        file.close()

                        keepLooping = input("\nAnother film to add? yes/no: ")
                        if keepLooping == "no":
                            break
                    
                # this on is for removing a film      faze._11
                elif choice == "3":
                    while True:
                        try:
                            file = open_file("films.dat", "rb")
                            films = pickle.load(file)

                            print("\nFilms Currently Showing:\n".upper())
                            for key in sorted(films.keys()):
                                print(key)
                                  
                            file.close()
                        except EOFError:
                            print("File is empty. You must add a film first before you can remove it. ")

                        filmToDelete = input("\nEnter the film title to delete: ")

                        try:
                            del films[filmToDelete];
                        except KeyError:
                            print("That film doesn't exist. STUPID \U0001f600 \U0001f600")

                        file = open_file("films.dat", "wb")
                        pickle.dump(films, file)
                        file.close()

                        keepLooping = input("\nAnother film to delete? yes/no: ")
                        if keepLooping == "no":
                            break
                    
                # if the manger is an idiot too LOLZZ    faze._11
                else:
                    print("Sorry, but ", choice, "isn't a valid choice.\n")

        # this on is for adding/removing screens          faze._11
        elif choice == "3":
            choice = None
            while choice != "0":
                # الحته دي عظمه       lolzzz           faze._11
                print(
        """
What would you like to do?

0 - Exit
1 - View Screens
2 - Add Screen
3 - Remove Screen
"""
                )

                choice = input("Choice: ")
                print()

                # this one is for exiting   faze._11
                if choice == "0":
                    print("Wait.....")

                # this one is for exiting   faze._11
                elif choice == "1":
                    try:
                        file = open_file("screens.dat", "rb")
                        screens = pickle.load(file)

                        print("\nThe following screens are in the file:\n")
                        for key, value in sorted(screens.items()):
                            print("Screen", key, "Capacity: ", value)
                                  
                        file.close()
                    except EOFError:
                        print("File is empty.")

                    input("\nPress the enter key to continue.")
                    print("\n")
                        
                # this on is for adding a screen    faze._11
                elif choice == "2":
                    while True:
                        ScreenNum = int(input("\nEnter the screen number: "))
                        Capacity = input("Enter the capacity: ")

                        try:
                            file = open_file("screens.dat", "rb")
                            screens = pickle.load(file)
                            file.close()
                        except EOFError:
                            screens = {}
                    
                        screens[ScreenNum] = Capacity
                    
                        file = open_file("screens.dat", "wb")
                        pickle.dump(screens, file)
                        file.close()

                        keepLooping = input("\nAnother screen to add? yes/no: ")
                        if keepLooping == "no":
                            break
                    
                #this one is for removing a screen      faze._11
                elif choice == "3":
                    while True:
                        try:
                            file = open_file("screens.dat", "rb")
                            screens = pickle.load(file)

                            print("\nThe following screens are in the file:\n")
                            for key, value in sorted(screens.items()):
                                print("Screen", key, "Capacity: ", value)
                                  
                            file.close()
                        except EOFError:
                            print("File is empty. You must add a screen first before you can remove it STUPID MANAGGER \U0001f600 \U0001f600. .")

                        screenToDelete = int(input("\nEnter the screen number to delete: "))

                        try:
                            del screens[screenToDelete];
                        except KeyError:
                            print("That screen doesn't exist. STUPID MANAGGER \U0001f600 \U0001f600..")
                            

                        file = open_file("screens.dat", "wb")
                        pickle.dump(screens, file)
                        file.close()

                        keepLooping = input("\nAnother screen to delete? yes/no: ")
                        if keepLooping == "no":
                            break
                    
                # the manger is being idiot again
                else:
                    print("Sorry, but ", choice, "isn't a valid choice.\n")

        # this one is for adding/removing showing         faze._11
        elif choice == "4":
            choice = None
            while choice != "0":
                # الحته دي عظمه       lolzzz           faze._11

                print(
        """
What would you like to do?

0 - Exit
1 - View Showings
2 - Add Showing
3 - Remove Showing
"""
                )

                choice = input("Choice: ")
                print()

                # this on is for exit       faze._11
                if choice == "0":
                    print("Exiting menu...")

                # this one is for viewing showings      faze._11
                elif choice == "1":
                    try:
                        file = open_file("showings.dat", "rb")
                        showings = pickle.load(file)

                        print("\nFilms Currently Showing:\n".upper())
                        for key, value in sorted(showings.items()):
                            print(key)
                            print("Screen:  ", "Date:  ", "           Time:  ")
                            for item in value:
                                for lowlist in item:
                                    print(lowlist, end="         ")
                                print("\n")
                        print("\n")
                                     
                        file.close()
                    except EOFError:
                        print("File is empty.")

                    input("\nPress the enter key to continue.")
                    print("\n")
                        
                # this one is for adding a showing       faze._11
                elif choice == "2":
                    while True:
                        try:
                            file = open_file("films.dat", "rb")
                            films = pickle.load(file)

                            print("\nFilms Currently Showing:\n".upper())
                            for key in sorted(films.keys()):
                                print(key)
                                  
                            file.close()
                        except EOFError:
                            print("File is empty.")

                        film = str(input("\nEnter the film showing: "))

                        try:
                            file = open_file("screens.dat", "rb")
                            screens = pickle.load(file)

                            print("\nThe following screens are in the file:\n")
                            for key, value in sorted(screens.items()):
                                print("Screen", key, "Capacity: ", value)
                                  
                            file.close()
                        except EOFError:
                            print("File is empty.")

                        screen = str(input("\nEnter the screen: "))

                        date = str(input("\nEnter the showing date, DD/MM/YYYY: "))
                        time = str(input("Enter the showing time, HH:MM : "))

                        try:
                            file = open_file("showings.dat", "rb")
                            showings = pickle.load(file)
                            file.close()
                        except EOFError:
                            showings = {}

                        details = [screen,date,time]
                    
                        showings.setdefault(film,[]).append(details)
                                        
                        file = open_file("showings.dat", "wb")
                        pickle.dump(showings, file)
                        file.close()

                        keepLooping = input("\nAnother showing to add? yes/no: ")
                        if keepLooping == "no":
                            break
                      
                # this one is for removing a showing      faze._11
                elif choice == "3":
                    while True:
                        try:
                            file = open_file("showings.dat", "rb")
                            showings = pickle.load(file)

                            print("\nFilms Currently Showing:\n".upper())
                            for key, value in sorted(showings.items()):
                                print(key)
                                print("Screen:  ", "Date:  ", "           Time:  ")
                                for item in value:
                                    for lowlist in item:
                                        print(lowlist, end="         ")
                                    print("\n")
                            print("\n")
                               
                            file.close()
                        except EOFError:
                            print("File is empty. You must add a showing first before you can remove it.")

                        print("\nFill in the following information for the showing you wish to delete.")
                        screenToDelete = str(input("\nEnter the screen: "))
                        dateToDelete = str(input("Enter the showing date, DD/MM/YYYY: "))
                        timeToDelete = str(input("Enter the showing time, HH:MM : "))

                        valueToDelete = [screenToDelete,dateToDelete,timeToDelete]

                        for value in showings.values():
                            try:
                                value.remove(valueToDelete)
                            except ValueError:
                                pass
                            
                        file = open_file("showings.dat", "wb")
                        pickle.dump(showings, file)
                        file.close()

                        keepLooping = input("\nAnother showing to delete? yes/no: ")
                        if keepLooping == "no":
                            break

                        print("\n")
                                            
                # again the same idiot lol
                else:
                    print("Sorry, but ", choice, "isn't a valid choice.\n")          

        # this one is for viewing tickets sold & income            faze._11
        elif choice == "5":
            try:
                file = open_file("tickets_sold.dat", "rb")
                tickets_sold = pickle.load(file)
                adult_sold = tickets_sold["AdultSold"]
                child_sold = tickets_sold["ChildSold"]
                concession_sold = tickets_sold["ConcessionSold"]
                total_taken = tickets_sold["TotalTaken"]
                file.close()

                print("Adult tickets sold: ", adult_sold)
                print("Child tickets sold: ", child_sold)
                print("Concession tickets sold: ", concession_sold)
                print("Total Money taken: L.E", "%.2f" % total_taken)
            except EOFError:
                print("File is empty. No tickets have been sold sadly.")

            input("\nPress the enter key to continue.\n")

        # IDIOTSSS
        else:
            print("Sorry, but '", choice, "' isn't a valid choice.\n")

def main():

    choice = None
    while choice != "0":
        # الحته دي عظمه       lolzzz           faze._11

        print(
        """
\t\tCinema Booking System


Who would you like to login as?

Please enter one of the options below.

0 - Exit
1 - Customer
2 - Manager (password required)
"""
            )

        choice = input("Choice: ")
        print()

        # this one is for exiting         faze._11
        if choice == "0":
            print("Exiting program...")

        # this on if the user entered customer menu        faze._11
        elif choice == "1":
            customer()

        # this on if the user entered enter manager menu       faze._11
        elif choice == "2":
            entered_password = input("Enter your password: ")
            if password(entered_password):
                manager()
            else:
                print("\nSorry, the password you entered was incorrect." \
                      "\nExiting to Main Menu...\n\n")


        else:
            print("Sorry, but '", choice, "' isn't a valid choice.\n")

main()
time.sleep(2)

# IDk what to call this lol and ,thanks if you are you still reading this , I hope you enjoyed this
# This is my instagram (faze._11) I guess you have this alot
# Have a great day or night idk frrrrrrrr LOLZZ

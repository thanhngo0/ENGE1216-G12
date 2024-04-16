"""
Main method that is intiailly called
Gives the user the available options for use
Once an option is choosen, the correct method is then
callled
"""
def main():
    print("----------------------------------------")
    print("1: Dimensions of the ladder extension")
    print("2: Space available for storage")
    print("3: Both 1 & 2")
    print("4: That's All. Thank you!")
    print("----------------------------------------")
    print("                                        ")
    which = int(input("What are you looking for? (type 1, 2, 3, or 4) "))
    if which == 1:
        dimensionsofshape()
        main()
    elif which == 2:
        storagespace()
        main()
    elif which == 3:
        dimensionsofshape()
        storagespace()
        main()
    elif which == 4:
        print("Have a good day!")
    else:
        print("Please input 1, 2, or 3")
        main()

"""
Determines if the ladder extension will be able to go on the 
ladder. It asks the user for the width of the ladder and then 
determines if the extension will fit on said ladder.

It also gives dimensions for the storage of the extension as well as
the volume and surface area of the extension as a whole based on user
inputted dimensions.
"""
def dimensionsofshape():
    print("                                     ")
    print("=====================================")
    print("                                     ")
    width = float(
        input("How wide is the ladder the extension will be installed on? (in inches) ")
    )
    print("                                     ")
    if width < 18:
        print("The width is too small for a ladder extension")
        print("Please try again")
        print("                                     ")
        dimensionsofshape()
    elif width < 20:
        print(
            "The extension will be 8 inches long and 5 inches high, with these options for the width:\n18 inches"
        )
    elif width < 22:
        print(
            "The extension will be 8 inches long and 5 inches high, with these options for the width:\n18 inches\n20 inches"
        )
    else:
        print(
            "The extension will be 8 inches long and 5 inches high, with these options for the width:\n18 inches\n20 inches\n22 inches"
        )
    option = float(input("What width would you like the extension to be? (in inches) "))
    if option == 18:
        print(
            "You have chosen the 18 inch wide extension, the storage area will 4.75 inches long, 17 inches wide, and 4 inches high.\nThe volume will be 332.56 in^3 and the surface area will be 991.59 in^2"
        )
    if option == 20:
        print(
            "You have chosen the 20 inch wide extension, the storage area will 4.75 inches long, 19 inches wide, and 4 inches high.\nThe volume will be 368.56 in^3 and the surface area will be 1094.59 in^2"
        )
    if option == 22:
        print(
            "You have chosen the 22 inch wide extension, the storage area will 4.75 inches long, 21 inches wide, and 4 inches high.\nThe volume will be 400.23 in^3 and the surface area will be 1181.69 in^2"
        )

"""
Asks the user for the dimesions of the extension (which can be aquired via dimensionsofshape
method or by user knowledge) and returns the volume of the storage. 

If the user wants to add an insert in the storage area then they can specify that when the method
asks that of them. If they do want an insert, then the method will ask for the dimensions of the insert
and then it will return the volume above and below the insert. 
"""
def storagespace():
    print("                                     ")
    print("=====================================")
    print("                                     ")
    width = float(input("How wide is the base of the ladder storage area? (in inches)"))
    print("                                     ")
    baselength = float(
        input("How long is the base of the ladder storage area? (in inches)")
    )
    print("                                     ")
    height = float(
        input("How tall are the sides of the ladder storage area? (in inches)")
    )
    print("                                     ")
    volumeofstorage = width * baselength * height #volume of storage with insert

    insert = str(
        input(
            "Is there an insert that will be placed inside of the storage area? (yes or no)"
        )
    )
    #if the user wants an insert
    if insert == "yes":
        print("                                     ")
        insertthickness = float(
            input("What is the thickness of the insert? (in inches)")
        )
        print("                                     ")
        insertheight = float(
            input(
                "How many inches up the side of the storage area will the insert be placed?"
            )
        )
        volumeabove = baselength * width * (height - (insertthickness + insertheight)) #volume of storage above the insert
        volumebelow = baselength * width * (insertheight) #volume below the insert

        print("The available space above the insert is: " + str(volumeabove) + " in^3")
        print("The available space below the insert is: " + str(volumebelow) + " in^3")
    #if the user does not want an insert
    elif insert == "no" or "n" or "nah":
        print("                                     ")
        print(
            "The available space in the ladder extension is: "
            + str(volumeofstorage)
            + " in^3"
        )
        print("                                     ")


main() #This is where the main method is called

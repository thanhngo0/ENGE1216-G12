"""
This is the intial prompt that asks the user for 
what they want to see. 
"""
def main():

    print("----------------------------------------")
    print("1: Dimensions of the ladder extension")
    print("2: Space available for storage")
    print("3: Both 1 & 2")
    print("4: That's All. Thank you!")
    print("----------------------------------------")
    print("                                        ")
    which = int(input("What are you looking for? (type 1, 2, 3, or 4)"))
    if which == 1: 
        dimensionsofshape()
    elif which == 2:
        storagespace()
    elif which == 3:
        dimensionsofshape()
        storagespace()
    elif which == 4:
        print("Have a good day!")
    else:
        print("Please input 1, 2, or 3")
        main()



def dimensionsofshape():{}
    #determines the shape of the build

"""
Determines the available space in the storage
First it asks for the dimensions of the storage then
asks if there is an insert in the storage
"""
def storagespace():
    print("                                     ")
    print("=====================================")
    print("                                     ")
    width = float(input("How wide is the base of the ladder storage area? (in inches)"))
    print("                                     ")
    baselength = float(input("How long is the base of the ladder storage area? (in inches)"))
    print("                                     ")
    height = float(input("How tall are the sides of the ladder storage area? (in inches)"))
    print("                                     ")
    volumeofstorage = width * baselength * height #this finds the volume

    insert = str(input("Is there an insert that will be placed inside of the storage area? (yes or no)")) #determines if there is an insert in the storage unit
    
    #If there is an insert in the storage
    if insert == "yes":
        print("                                     ")
        insertthickness = float(input("What is the thickness of the insert? (in inches)"))
        print("                                     ")
        insertheight = float(input("How many inches up the side of the storage area will the insert be placed?"))
        
        volumeabove = baselength * width * (height - (insertthickness + insertheight)) #volume above the insert
        volumebelow = baselength * width * (insertheight) #volume below the insert

        print ("The available space above the insert is: " + str(volumeabove) + " in^3" )
        print ("The available space below the insert is: " + str(volumebelow) + " in^3" )

    #if there is no insert
    elif insert == "no" or "n" or "nah":
        print("                                     ")
        print ("The available space in the ladder extension is: " + str(volumeofstorage) + " in^3" )
        print("                                     ")
        main()

#calls the intial function
main()

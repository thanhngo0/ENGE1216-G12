def main():
    print("1: dimensions of the ladder extension")
    print("2: space available for storage")
    print("3: Both")
    which = int(input("What are you looking for? (type 1, 2, or 3)"))
    if which == 1: 
        dimensionsofshape()
    elif which == 2:
        storagespace()
    elif which == 3:
        dimensionsofshape()
        storagespace()
    else:
        print("Please input 1, 2, or 3")
        main()



def dimensionsofshape():{
    
    #determines the shape of the build
    }

def storagespace():{
    basewidth = int(input("How wide is the base of the ladder storage area? (in inches)"))
    baselength = int(input("How long is the base of the ladder storage area? (in inches)"))
    height = int(input("How tall are the sides of the ladder storage area? (in inches)"))

    volumeofstorage = basewidth * baselength * height

    insert = str(input("Is there an insert that will be placed inside of the storage area? (yes or no)"))

    if insert == "yes" or "y" or "yeah":
        insertthickness = int(input("What is the thickness of the insert? (in inches)"))
        insertheight = int(input("How many inches up the side of the storage area will the insert be placed?"))
        
        volumeabove insert = baselength * basewidth * (height - (thickness + insertheight))
        volumebelow = baselength * basewidth * (insertheight)

        print ("The available space above the insert is: " + str(volumeabove) + " in^3" )
        print ("The available space below the insert is: " + str(volumebelow) + " in^3" )

    elif insert == "no" or "n" or "nah":
        print ("The available space in the ladder extension is: " + str(volumeofstorage) + " in^3" )
}
main()

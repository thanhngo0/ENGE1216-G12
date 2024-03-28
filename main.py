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
    print(1)
    #determines the shape of the build
    }

def storagespace():{
    print(2)
    #determine how much storage is available
}
main()

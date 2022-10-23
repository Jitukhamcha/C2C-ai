disc_count=int(input("Enter desired amount of disc: "))

def TowerOfHanoi(n,tw_source,tw_destination,tw_medium):
    if(n>0):
        #moving n-1 discs from A(source) to B(medium) using C(destination) recursively
        TowerOfHanoi(n-1,tw_source,tw_medium,tw_destination)
        #moving nth disc from A(source) to C(destination)
        print(f"Move {n} from {tw_source} to {tw_destination} ")
        #moving n-1 discs from B(medium) to C(Destination) using A(source) recursively
        TowerOfHanoi(n-1,tw_medium,tw_destination,tw_source)
        
TowerOfHanoi(disc_count,'A','C','B')
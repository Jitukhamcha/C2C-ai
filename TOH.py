#the goal is to move all disks form source to destination
#large disk can't be placed over smaller disk

#funtion body
def Tower_Hanoi(n,source,helper,destination):
    if n==1 :
        print("moving disk 1 from rod {} to rod {}.".format(source,destination))
        return
    Tower_Hanoi(n-1,source,destination,helper)
    print("moving disk {} from rod {} to rod {}.".format(n,source,destination))
    Tower_Hanoi(n-1,helper,source,destination)

#input section
n = int(input('Enter the number of disk:'))

#calling funciton
Tower_Hanoi(n,'A','B','C')


def isSorted(lst):
    i=1
    while i < len(lst):
        if(lst[i]< lst[i-1]):
            return False
        i+=1
    return True



def main():
    s=input("Enter list: ")
    items=s.split()
    list1=[eval(x) for x in items]

    if isSorted(list1):
        print("The list is already sorted")
    else:
        print("The list is not sorted")

main()

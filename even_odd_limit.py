def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i, "Even")
        else :
            print(i, "Odd")


(x) = int(input("enter :"))
print(showNumbers(x))
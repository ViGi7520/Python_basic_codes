def shownumbers(start, end):
    for i in range(start, end+1):
        if i % 2 == 0:
            print(i, "Even")
        else:
            print(i, "Odd")


start = int(input('Enter the Start : '))
end = int(input('Enter the End : '))
print(shownumbers(start, end))

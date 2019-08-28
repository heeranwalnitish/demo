x =10
for row in range(x):
    #code for letter N
    for col in range(x):
        if col == 0 or col == x-1 or (row==col):
            print("*",end ='')
        else:
            print(end =" ")

    #code for letter I
    for col in range(1):
        print("    *    ",end = '')

    #Code fo rletter T
    for col in range(x):
        if col==(x/2) or row == 0:
            print("*", end ='')
        else :
            print(" ",end = "")

    #code for letter I
    for col in range(1):
        print("    *    ",end = '')

    #Code for letter S
    for col in range(x):
        if (row ==0 or row == x/2 or row == x-1  or (col == 0 and (row>0 and row<x/2)) or (col==x-1 and((row>x/2) and(row<x-1)))):
            print("*", end ='')

        else:
            print(" ",end ='')

    # code for maintaining Space
    for col in range(1):
         print("    ", end='')

    #code for letter H
    for col in range(x):
        if col == 0 or col == x - 1 or row == x / 2:
            print("*", end='')
        else:
            print(" ", end='')

    print()


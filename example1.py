print("Welcome to use Prime Number Detector")
print("Version 1.0.1")
iteration = True

while iteration :
    Prime = True
    Factor = 0

    Number = input("Enter the Integer needed to be tested (Enter 0 to exit the Program): \n")

    if (Number.isdigit()):
        Number = int(Number)
        if Number != 0:
            Factor_List = []
            j = int(Number/2)+1
            for i in range(2, j):
                if Number % i == 0:
                    Factor_List.append(i)
                    Prime = False
                j = int(j/i)
            if Prime == True:
                print(str(Number) + " is Prime!")
            if Prime == False:
                # print(Factor_List)
                print(str(Number) + " is not Prime, it has factor " + str(Factor_List))

        else:
            iteration = False;
            print("Thank you for using Prime Number Detector")

    else:
        print("It's not an integer, please enter an **Integer** !")

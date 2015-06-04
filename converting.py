# Converting datatypes
# The W is for write mode, A is for append and R is for read


myBool = True
while myBool == True:
    myVal = input("Please enter a number to add: \n")
    myString = str(myVal)
    myFile = open("thisFile.txt", "a")
    myFile.write("\n" + myString)
    repeat = input("Enter another? \n")
    if repeat == "y":
        myBool = True
    else:
        myBool = False
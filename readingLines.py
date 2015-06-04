# Reading lines from a text file:

myFile = open('thisFile.txt')
for line in myFile.readlines():
    print(line)
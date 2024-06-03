#Write a program that opens the things.txt file that was created by the program in problem 1,
# reads all of the data from the file before closing it, and then displays the data from the file.

fo = open("things.txt", "r+")
str = fo.read()
print("Read String is : ", str)
fo.close()
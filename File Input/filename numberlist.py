# Write code that does the following: Opens an output file with the filename number_list.txt,
# uses a loop to write the numbers 1 through 100 to the file, then closes the file.


File_navn = input("indtast navnet på filen, med ekstensions!")

with open("number_list.txt", "w") as file:
    for number in range(1, 101,4):
        file.write(f"{number}\n")

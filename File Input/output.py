# Write a program that opens an output file with the file name things.txt,
# writes the name of an animal, a fruit and a country to the file on separate lines, then closes the file.

if __name__ == "__main__":
    File_navn = input("indtast navnet på filen, med ekstensions!")
    f = open(File_navn, "w")  # Filen oprettes og hvis der eksistere en i forvejen overskrives den!

    string1 = input("Indtast et navn på et dyr")
    string1 = string1 + "\n"
    string2 = input("indtast et navn på en frugt")
    string2 = string2 + "\n"
    string3 = input("indtast et navn på et land")
    string3 = string3 + "\n"

    f.write(string1 + string2 + string3)
    f.close()

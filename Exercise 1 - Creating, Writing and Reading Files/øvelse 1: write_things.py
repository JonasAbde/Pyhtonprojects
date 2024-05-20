# Øvelse - Oprettelse, skrivning og læsning af filer
# 1. Skriv et program, der åbner en outputfil med navnet things.txt, hvor brugeren kan indtaste navnet på et dyr, en frugt og et land i filen på separate linjer, og derefter lukker filen.

if __name__ == "__main__":
    # Brugeren indtaster navnet på filen
    File_navn = input("Indtast navnet på filen, med ekstensions: ")
    f = open(File_navn, "w")  # Filen oprettes, og hvis der eksisterer en i forvejen, overskrives den

    # Brugeren indtaster navnet på et dyr, en frugt og et land
    dyr = input("Indtast navnet på et dyr: ")
    frugt = input("Indtast navnet på en frugt: ")
    land = input("Indtast navnet på et land: ")

    # Skriver data til filen
    f.write(dyr + "\n")
    f.write(frugt + "\n")
    f.write(land + "\n")
    f.close()  # Filen lukkes ned

    # Åbn filen som er i projektmappen, og se om den indeholder den tekst, du skrev.
    print(f"Data er blevet skrevet til {File_navn}. Åbn filen for at se indholdet.")

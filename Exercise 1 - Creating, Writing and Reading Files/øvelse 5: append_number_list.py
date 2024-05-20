# Øvelse - Oprettelse, skrivning og læsning af filer
# 5. Skriv kode, der åbner en outputfil med navnet number_list.txt, men ikke sletter filens indhold, hvis den allerede eksisterer.

if __name__ == "__main__":
    # Brugeren indtaster navnet på filen
    File_navn = input("Indtast navnet på filen, med ekstensions: ")

    f = None
    try:
        # Åbner filen number_list.txt i tilføjelsesmodus ("a")
        f = open(File_navn, "a")

        # Tilføjer nye numre til filen
        for number in range(101, 111):
            f.write(f"{number}\n")

        print(f"Data er blevet tilføjet til {File_navn}.")
    except Exception as e:
        print(f"En fejl opstod: {e}")
    finally:
        if f:
            f.close()  # Filen lukkes ned

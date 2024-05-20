# Øvelse - Oprettelse, skrivning og læsning af filer
# 4. Skriv kode, der gør følgende: Åbner number_list.txt, der blev oprettet af koden fra problem 3, læser alle numrene fra filen og viser dem, og derefter lukker filen.

if __name__ == "__main__":
    # Brugeren indtaster navnet på filen
    File_navn = input("Indtast navnet på filen, med ekstensions: ")

    f = None
    try:
        # Åbner filen number_list.txt i læsetilstand ("r")
        f = open(File_navn, "r")

        # Læser alle numrene fra filen linje for linje
        for line in f.readlines():
            print(f"Læser: {line.strip()}")

    except FileNotFoundError:
        print(f"Filen {File_navn} blev ikke fundet.")
    finally:
        if f:
            f.close()  # Filen lukkes ned

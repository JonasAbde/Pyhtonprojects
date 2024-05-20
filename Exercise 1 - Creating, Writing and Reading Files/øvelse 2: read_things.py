# Øvelse - Oprettelse, skrivning og læsning af filer
# 2. Skriv et program, der åbner filen things.txt, som blev oprettet af programmet i problem 1, læser al data fra filen, før den lukkes, og derefter viser dataen fra filen.

if __name__ == "__main__":
    # Brugeren indtaster navnet på filen
    File_navn = input("Indtast navnet på filen, med ekstensions: ")

    f = None
    try:
        # Åbner filen things.txt i læsetilstand ("r")
        f = open(File_navn, "r")

        # Læser al data fra filen
        data = f.read()

        # Viser dataen
        print("Indholdet af things.txt:")
        print(data)
    except FileNotFoundError:
        print(f"Filen {File_navn} blev ikke fundet.")
    finally:
        if f:
            f.close()  # Filen lukkes ned

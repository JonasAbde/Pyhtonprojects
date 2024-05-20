# Øvelse - Oprettelse, skrivning og læsning af filer
# 2. Skriv et program, der beder brugeren om et filnavn. Programmet skal vise indholdet af filen med hver linje forudgået af et linjenummer efterfulgt af et kolon. Linjenummereringen skal starte ved 1.

if __name__ == "__main__":
    # Brugeren indtaster navnet på filen
    File_navn = input("Indtast navnet på filen, med ekstensions: ")

    f = None
    try:
        # Åbner filen i læsetilstand ("r")
        f = open(File_navn, "r")

        # Læser filen linje for linje og viser linjenummeret foran hver linje
        line_number = 1
        for line in f:
            print(f"{line_number}: {line.strip()}")
            line_number += 1

    except FileNotFoundError:
        print(f"Filen {File_navn} blev ikke fundet.")
    except Exception as e:
        print(f"En fejl opstod: {e}")
    finally:
        if f:
            f.close()  # Filen lukkes ned

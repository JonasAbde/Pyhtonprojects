# Øvelse - Oprettelse, skrivning og læsning af filer
# 3. Skriv kode, der gør følgende: Åbner en outputfil med navnet number_list.txt, bruger en løkke til at skrive tallene 1 til 100 til filen og derefter lukker filen.

if __name__ == "__main__":
    # Brugeren indtaster navnet på filen
    File_navn = input("Indtast navnet på filen, med ekstensions: ")

    try:
        # Åbner filen number_list.txt i skrivemode ("w")
        f = open(File_navn, "w")

        # Skriver tallene 1 til 100 til filen
        for number in range(1, 101):
            f.write(f"{number}\n")

        print(f"Data er blevet skrevet til {File_navn}.")
    except Exception as e:
        print(f"En fejl opstod: {e}")
    finally:
        if f:
            f.close()  # Filen lukkes ned

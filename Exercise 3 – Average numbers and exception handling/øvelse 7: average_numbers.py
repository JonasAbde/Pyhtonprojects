# Øvelse - Oprettelse, skrivning og læsning af filer
# 3. Antag, at en fil, der indeholder en række heltal, hedder numbers.txt og findes på computerens disk.
# Skriv et program, der beregner gennemsnittet af alle de tal, der er gemt i filen.
# Modificer programmet, så det håndterer følgende undtagelser:
# - Håndterer enhver IOError-undtagelse, der opstår, når filen åbnes og data læses fra den
# - Håndterer enhver ValueError-undtagelse, der opstår, når elementerne, der læses fra filen, konverteres til et tal

if __name__ == "__main__":
    try:
        # Åbner filen numbers.txt i læsetilstand ("r")
        with open("numbers.txt", "r") as f:
            numbers = f.readlines()

        total = 0
        count = 0

        for line in numbers:
            try:
                number = int(line.strip())
                total += number
                count += 1
            except ValueError:
                print(f"Advarsel: Kunne ikke konvertere linjen til et tal: {line.strip()}")

        if count > 0:
            average = total / count
            print(f"Gennemsnittet af tallene i filen er: {average}")
        else:
            print("Ingen gyldige tal blev fundet i filen.")

    except IOError:
        print("Fejl: Kunne ikke åbne eller læse filen numbers.txt.")
    except Exception as e:
        print(f"En uventet fejl opstod: {e}")

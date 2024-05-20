def tjek_temperatur():
    """Spørger brugeren om en temperatur og foreslår at åbne et vindue, hvis den er over 25 grader."""

    while True:
        try:
            temperatur = float(input("Indtast temperaturen i grader Celsius: "))
            break  # Afslut løkken, hvis indtastningen er gyldig
        except ValueError:
            print("Ugyldig indtastning. Indtast venligst et tal.")

    if temperatur > 25:
        print("Det er varmt! Overvej at åbne et vindue.")
    # Du kan tilføje en else-del her, hvis du vil have en besked til lavere temperaturer.

if __name__ == "__main__":
    tjek_temperatur()

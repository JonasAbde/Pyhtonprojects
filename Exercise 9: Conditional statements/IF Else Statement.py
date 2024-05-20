def tjek_temperatur_og_vindue():
    """
    Spørger brugeren om temperaturen og foreslår at åbne eller lukke vinduet afhængigt af temperaturen.
    """

    while True:
        try:
            temperatur = float(input("Indtast temperaturen i grader Celsius: "))
            break
        except ValueError:
            print("Ugyldig indtastning. Indtast venligst et tal.")

    if temperatur > 25:
        print("Det er varmt! Overvej at åbne et vindue.")
    else:
        print("Det er køligt nok til at lukke vinduet, hvis det er åbent.")

if __name__ == "__main__":
    tjek_temperatur_og_vindue()

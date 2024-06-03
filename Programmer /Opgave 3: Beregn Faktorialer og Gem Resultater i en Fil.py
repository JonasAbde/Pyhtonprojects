# Opgavebeskrivelse:
# Skriv et program, der læser tal fra en fil, beregner faktorialen for hvert tal,
# og skriver resultaterne til en ny fil.

def læs_tal_fra_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            tal = [int(linje.strip()) for linje in fil]
        return tal
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")
        return []
    except ValueError:
        print("Filen indeholder ikke gyldige tal.")
        return []

def skriv_resultater_til_fil(filnavn, resultater):
    with open(filnavn, 'w') as fil:
        for resultat in resultater:
            fil.write(f"{resultat}\n")

def beregn_faktorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

# Hovedprogram
input_filnavn = 'tal.txt'
output_filnavn = 'faktorial_resultater.txt'

tal = læs_tal_fra_fil(input_filnavn)
resultater = [f"{t}: {beregn_faktorial(t)}" for t in tal]

skriv_resultater_til_fil(output_filnavn, resultater)
print(f"Faktorialerne er skrevet til {output_filnavn}.")

# Hvad der sker:
# - læs_tal_fra_fil() funktionen læser tal fra en fil og returnerer dem som en liste.
# - beregn_faktorial() funktionen beregner faktorialen for et tal.
# - skriv_resultater_til_fil() funktionen skriver en liste af resultater til en fil.
# - Hovedprogrammet kombinerer disse funktioner for at læse tal fra 'tal.txt', beregne faktorialen for hvert tal,
#   og skrive resultaterne til 'faktorial_resultater.txt'.

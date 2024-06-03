# Opgavebeskrivelse:
# Skriv et program, der læser ord fra en fil, tjekker om hvert ord er et palindrom,
# og skriver resultatet til en ny fil.

def læs_ord_fra_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            ord = [linje.strip() for linje in fil]
        return ord
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")
        return []

def skriv_resultater_til_fil(filnavn, resultater):
    with open(filnavn, 'w') as fil:
        for resultat in resultater:
            fil.write(f"{resultat}\n")

def er_palindrom(ord):
    return ord == ord[::-1]

# Hovedprogram
input_filnavn = 'ord.txt'
output_filnavn = 'palindrom_resultater.txt'

ord = læs_ord_fra_fil(input_filnavn)
resultater = [f"{o}: {'palindrom' if er_palindrom(o) else 'ikke palindrom'}" for o in ord]

skriv_resultater_til_fil(output_filnavn, resultater)
print(f"Resultaterne er skrevet til {output_filnavn}.")

# Hvad der sker:
# - læs_ord_fra_fil() funktionen læser ord fra en fil og returnerer dem som en liste.
# - er_palindrom() funktionen tjekker, om et ord er et palindrom.
# - skriv_resultater_til_fil() funktionen skriver en liste af resultater til en fil.
# - Hovedprogrammet kombinerer disse funktioner for at læse ord fra 'ord.txt', tjekke om hvert ord er et palindrom,
#   og skrive resultaterne til 'palindrom_resultater.txt'.

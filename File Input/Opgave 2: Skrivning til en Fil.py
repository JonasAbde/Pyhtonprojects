# Opgavebeskrivelse:
# Skriv et program, der åbner en fil til skrivning, og skriver hver streng fra en liste til filen på en ny linje.

def skriv_til_fil(filnavn, linjer):
    with open(filnavn, 'w') as fil:
        for linje in linjer:
            fil.write(linje + '\n')

# Eksempel brug
filnavn = 'output.txt'
linjer = ['Dette er linje 1', 'Dette er linje 2', 'Dette er linje 3']
skriv_til_fil(filnavn, linjer)

# Hvad der sker:
# - open(filnavn, 'w') åbner filen 'filnavn' i skrivemodus (og opretter den, hvis den ikke findes).
# - with open(filnavn, 'w') as fil sikrer, at filen lukkes korrekt efter skrivning.
# - for linje in linjer itererer gennem hver streng i listen 'linjer'.
# - fil.write(linje + '\n') skriver hver streng til filen efterfulgt af en ny linje.

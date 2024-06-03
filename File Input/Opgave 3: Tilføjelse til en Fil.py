# Opgavebeskrivelse:
# Skriv et program, der åbner en fil til tilføjelse, og tilføjer flere linjer til filen.

def tilføj_til_fil(filnavn, linjer):
    with open(filnavn, 'a') as fil:
        for linje in linjer:
            fil.write(linje + '\n')

# Eksempel brug
filnavn = 'output.txt'
linjer = ['Dette er en ny linje 1', 'Dette er en ny linje 2']
tilføj_til_fil(filnavn, linjer)

# Hvad der sker:
# - open(filnavn, 'a') åbner filen 'filnavn' i tilføjelsesmodus.
# - with open(filnavn, 'a') as fil sikrer, at filen lukkes korrekt efter tilføjelse.
# - for linje in linjer itererer gennem hver streng i listen 'linjer'.
# - fil.write(linje + '\n') tilføjer hver streng til filen efterfulgt af en ny linje.
# - De nye
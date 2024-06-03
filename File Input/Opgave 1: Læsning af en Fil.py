# Opgavebeskrivelse:
# Skriv et program, der åbner en fil, læser dens indhold linje for linje og udskriver hver linje til skærmen.

def læs_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            for linje in fil:
                print(linje.strip())
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")

# Eksempel brug
filnavn = 'eksempel.txt'
læs_fil(filnavn)

# Hvad der sker:
# - open(filnavn, 'r') åbner filen 'filnavn' i læsemodus.
# - with open(filnavn, 'r') as fil sikrer, at filen lukkes korrekt efter læsning.
# - for linje in fil itererer gennem hver linje i filen.
# - linje.strip() fjerner eventuelle indledende og afsluttende mellemrum fra hver linje.
# - Hver linje udskrives til skærmen.

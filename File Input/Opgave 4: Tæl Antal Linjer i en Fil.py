# Opgavebeskrivelse:
# Skriv et program, der åbner en fil, tæller antallet af linjer og udskriver dette tal.

def tæl_linjer(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            antal_linjer = sum(1 for linje in fil)
        print(f"Antal linjer i filen: {antal_linjer}")
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")

# Eksempel brug
filnavn = 'eksempel.txt'
tæl_linjer(filnavn)

# Hvad der sker:
# - open(filnavn, 'r') åbner filen 'filnavn' i læsemodus.
# - with open(filnavn, 'r') as fil sikrer, at filen lukkes korrekt efter læsning.
# - sum(1 for linje in fil) tæller antallet af linjer i filen ved at iterere gennem hver linje.
# - Vi udskriver antallet af linjer i filen.

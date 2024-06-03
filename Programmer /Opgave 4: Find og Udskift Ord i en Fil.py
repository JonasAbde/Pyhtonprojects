# Opgavebeskrivelse:
# Skriv et program, der læser indholdet af en fil, finder og udskifter et bestemt ord med et andet ord,
# og skriver det opdaterede indhold til en ny fil.

def læs_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            indhold = fil.read()
        return indhold
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")
        return ""

def skriv_fil(filnavn, indhold):
    with open(filnavn, 'w') as fil:
        fil.write(indhold)

def find_og_udskift(indhold, gammelt_ord, nyt_ord):
    return indhold.replace(gammelt_ord, nyt_ord)

# Hovedprogram
input_filnavn = 'tekst.txt'
output_filnavn = 'opdateret_tekst.txt'
gammelt_ord = 'gammelt'
nyt_ord = 'nyt'

indhold = læs_fil(input_filnavn)
opdateret_indhold = find_og_udskift(indhold, gammelt_ord, nyt_ord)
skriv_fil(output_filnavn, opdateret_indhold)

print(f"Ordet '{gammelt_ord}' er erstattet med '{nyt_ord}' i filen '{output_filnavn}'.")

# Hvad der sker:
# - læs_fil() funktionen læser indholdet af en fil og returnerer det som en streng.
# - find_og_udskift() funktionen erstatter alle forekomster af 'gammelt_ord' med 'nyt_ord' i indholdet.
# - skriv_fil() funktionen skriver det opdaterede indhold til en ny fil.
# - Hovedprogrammet kombinerer disse funktioner for at læse indholdet af 'tekst.txt', udskifte et bestemt ord med et andet,
#   og skrive det opdaterede indhold til 'opdateret_tekst.txt'.

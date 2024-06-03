# Opgavebeskrivelse:
# Skriv et program, der åbner en fil, finder og udskifter et specifikt ord med et andet ord, og skriver ændringerne til en ny fil.

def find_og_udskift(filnavn, gammelt_ord, nyt_ord, nyt_filnavn):
    try:
        with open(filnavn, 'r') as fil:
            indhold = fil.read()
        nyt_indhold = indhold.replace(gammelt_ord, nyt_ord)
        with open(nyt_filnavn, 'w') as ny_fil:
            ny_fil.write(nyt_indhold)
        print(f"Ordet '{gammelt_ord}' er erstattet med '{nyt_ord}' i filen '{nyt_filnavn}'.")
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")

# Eksempel brug
filnavn = 'eksempel.txt'
gammelt_ord = 'gammelt'
nyt_ord = 'nyt'
nyt_filnavn = 'ny_fil.txt'
find_og_udskift(filnavn, gammelt_ord, nyt_ord, nyt_filnavn)

# Hvad der sker:
# - open(filnavn, 'r') åbner filen 'filnavn' i læsemodus og læser hele indholdet.
# - indhold.replace(gammelt_ord, nyt_ord) erstatter alle forekomster af 'gammelt_ord' med 'nyt_ord' i indholdet.
# - open(nyt_filnavn, 'w') åbner (eller opretter) en ny fil 'nyt_filnavn' i skrivemodus og skriver det opdaterede indhold til denne fil.
# - Vi udskriver en besked om, at udskiftningen er udført.

# Opgavebeskrivelse:
# Skriv et program, der åbner en fil, læser dens indhold og kopierer dette indhold til en anden fil.

def kopier_fil(fra_filnavn, til_filnavn):
    try:
        with open(fra_filnavn, 'r') as fra_fil:
            indhold = fra_fil.read()
        with open(til_filnavn, 'w') as til_fil:
            til_fil.write(indhold)
        print(f"Indholdet af {fra_filnavn} er kopieret til {til_filnavn}.")
    except FileNotFoundError:
        print(f"Filen {fra_filnavn} blev ikke fundet.")

# Eksempel brug
fra_filnavn = 'eksempel.txt'
til_filnavn = 'kopi.txt'
kopier_fil(fra_filnavn, til_filnavn)

# Hvad der sker:
# - open(fra_filnavn, 'r') åbner filen 'fra_filnavn' i læsemodus og læser hele indholdet.
# - open(til_filnavn, 'w') åbner (eller opretter) en ny fil 'til_filnavn' i skrivemodus og skriver det læste indhold til denne fil.
# - Vi udskriver en besked om, at kopieringen er udført.

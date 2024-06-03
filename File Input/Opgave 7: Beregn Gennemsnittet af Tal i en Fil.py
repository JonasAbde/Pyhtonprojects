# Opgavebeskrivelse:
# Skriv et program, der åbner en fil, læser talene fra filen og beregner gennemsnittet af disse tal.

def beregn_gennemsnit(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            tal = [int(linje.strip()) for linje in fil]
        if tal:
            gennemsnit = sum(tal) / len(tal)
            print(f"Gennemsnittet af tallene er: {gennemsnit}")
        else:
            print("Filen er tom.")
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")
    except ValueError:
        print("Filen indeholder ikke gyldige tal.")

# Eksempel brug
filnavn = 'tal.txt'
beregn_gennemsnit(filnavn)

# Hvad der sker:
# - open(filnavn, 'r') åbner filen 'filnavn' i læsemodus og læser tallene fra filen.
# - [int(linje.strip()) for linje in fil] konverterer hver linje til et heltal og gemmer dem i en liste.
# - sum(tal) / len(tal) beregner gennemsnittet af tallene i listen.
# - Vi udskriver gennemsnittet af tallene.
# - Hvis filen ikke findes, udskrives en fejlmeddelelse.
# - Hvis filen indeholder ugyldige tal, udskrives en fejlmeddelelse.

# Opgavebeskrivelse:
# Skriv et program, der læser tal fra en fil, filtrerer de positive tal, beregner gennemsnittet af de positive tal,
# og skriver både de filtrerede tal og gennemsnittet til en ny fil.

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

def skriv_tal_til_fil(filnavn, tal):
    with open(filnavn, 'w') as fil:
        for nummer in tal:
            fil.write(f"{nummer}\n")

def filtrer_positive_tal(tal):
    return [nummer for nummer in tal if nummer > 0]

def beregn_gennemsnit(tal):
    return sum(tal) / len(tal) if tal else 0

# Hovedprogram
input_filnavn = 'tal.txt'
output_filnavn = 'positive_tal.txt'

tal = læs_tal_fra_fil(input_filnavn)
positive_tal = filtrer_positive_tal(tal)
gennemsnit = beregn_gennemsnit(positive_tal)
positive_tal.append(f"Gennemsnit: {gennemsnit}")

skriv_tal_til_fil(output_filnavn, positive_tal)
print(f"Positive tal og gennemsnit er skrevet til {output_filnavn}.")

# Hvad der sker:
# - læs_tal_fra_fil() funktionen læser tal fra en fil og returnerer dem som en liste.
# - filtrer_positive_tal() funktionen filtrerer de positive tal fra listen.
# - beregn_gennemsnit() funktionen beregner gennemsnittet af en liste af tal.
# - skriv_tal_til_fil() funktionen skriver en liste af tal til en fil.
# - Hovedprogrammet kombinerer disse funktioner for at læse tal fra 'tal.txt', filtrere de positive tal,
#   beregne gennemsnittet af de positive tal og skrive resultatet til 'positive_tal.txt'.
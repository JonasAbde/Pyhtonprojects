# Opgavebeskrivelse:
# Skriv et program, der læser data fra en fil, sorterer dataene i stigende rækkefølge
# og skriver de sorterede data til en ny fil.

def læs_data_fra_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            data = [linje.strip() for linje in fil]
        return data
    except FileNotFoundError:
        print(f"Filen {filnavn} blev ikke fundet.")
        return []

def skriv_data_til_fil(filnavn, data):
    with open(filnavn, 'w') as fil:
        for item in data:
            fil.write(f"{item}\n")

# Hovedprogram
input_filnavn = 'data.txt'
output_filnavn = 'sorteret_data.txt'

data = læs_data_fra_fil(input_filnavn)
sorteret_data = sorted(data)
skriv_data_til_fil(output_filnavn, sorteret_data)

print(f"De sorterede data er skrevet til {output_filnavn}.")

# Hvad der sker:
# - læs_data_fra_fil() funktionen læser data fra en fil og returnerer dem som en liste af strenge.
# - sorted(data) sorterer listen af data i stigende rækkefølge.
# - skriv_data_til_fil() funktionen skriver de sorterede data til en ny fil.
# - Hovedprogrammet kombinerer disse funktioner for at læse data fra 'data.txt', sortere dataene,
#   og skrive de sorterede data til 'sorteret_data.txt'.

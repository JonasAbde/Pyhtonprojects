# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet år er et skudår og returnerer True, hvis det er, og False, hvis det ikke er.

def er_skudår(år):
    return (år % 4 == 0 and år % 100 != 0) or (år % 400 == 0)

# Eksempel brug
år = 2024
print(f"Er {år} et skudår? {er_skudår(år)}")

# Hvad der sker:
# - år % 4 == 0 tjekker, om året er deleligt med 4.
# - år % 100 != 0 tjekker, om året ikke er deleligt med 100 (for at udelukke år, der ikke er skudår).
# - år % 400 == 0 tjekker, om året er deleligt med 400 (for at inkludere år, der er skudår).
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde er_skudår() funktionen med 'år' som argument.

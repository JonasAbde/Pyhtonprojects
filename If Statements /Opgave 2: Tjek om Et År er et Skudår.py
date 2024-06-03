# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet år er et skudår og udskriver en passende besked.

def er_skudår(år):
    if (år % 4 == 0 and år % 100 != 0) or (år % 400 == 0):
        print(f"{år} er et skudår.")
    else:
        print(f"{år} er ikke et skudår.")

# Eksempel brug
er_skudår(2024)
er_skudår(2023)

# Hvad der sker:
# - Vi bruger en if-else struktur til at tjekke, om 'år' er et skudår.
# - Hvis 'år' er deleligt med 4, men ikke med 100, eller hvis det er deleligt med 400, udskrives en besked om, at 'år' er et skudår.
# - Ellers udskrives en besked om, at 'år' ikke er et skudår.

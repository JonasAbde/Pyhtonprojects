# Opgavebeskrivelse:
# Skriv et program, der tjekker om to tal er multipler af hinanden og udskriver en passende besked.

def er_multipler(tal1, tal2):
    if tal1 % tal2 == 0 or tal2 % tal1 == 0:
        print(f"{tal1} og {tal2} er multipler af hinanden.")
    else:
        print(f"{tal1} og {tal2} er ikke multipler af hinanden.")

# Eksempel brug
er_multipler(12, 4)
er_multipler(7, 3)

# Hvad der sker:
# - Vi bruger en if-else struktur til at tjekke, om 'tal1' er en multipel af 'tal2' eller omvendt.
# - Hvis tal1 % tal2 == 0 eller tal2 % tal1 == 0, udskrives en besked om, at de er multipler af hinanden.
# - Ellers udskrives en besked om, at de ikke er multipler af hinanden.

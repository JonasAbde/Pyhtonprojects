# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet bogstav er en vokal eller en konsonant og udskriver en passende besked.

def tjek_bogstav(bogstav):
    if bogstav.lower() in 'aeiou':
        print(f"{bogstav} er en vokal.")
    else:
        print(f"{bogstav} er en konsonant.")

# Eksempel brug
tjek_bogstav('A')
tjek_bogstav('b')

# Hvad der sker:
# - Vi bruger en if-else struktur til at tjekke, om 'bogstav' er en vokal.
# - Hvis 'bogstav' er en af 'a', 'e', 'i', 'o' eller 'u' (enten i små eller store bogstaver), udskrives en besked om, at 'bogstav' er en vokal.
# - Ellers udskrives en besked om, at 'bogstav' er en konsonant.


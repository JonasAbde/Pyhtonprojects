# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet tal er positivt, negativt eller nul og udskriver en passende besked.

def tjek_tal(tal):
    if tal > 0:
        print(f"{tal} er positivt.")
    elif tal < 0:
        print(f"{tal} er negativt.")
    else:
        print(f"{tal} er nul.")

# Eksempel brug
tjek_tal(5)
tjek_tal(-3)
tjek_tal(0)

# Hvad der sker:
# - Vi bruger en if-elif-else struktur til at tjekke værdien af 'tal'.
# - Hvis 'tal' er større end 0, udskrives en besked om, at 'tal' er positivt.
# - Hvis 'tal' er mindre end 0, udskrives en besked om, at 'tal' er negativt.
# - Hvis 'tal' er lig med 0, udskrives en besked om, at 'tal' er nul.

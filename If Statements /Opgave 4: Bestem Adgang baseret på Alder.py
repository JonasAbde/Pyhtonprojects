# Opgavebeskrivelse:
# Skriv et program, der bestemmer adgang baseret på alder og udskriver en passende besked.

def tjek_adgang(alder):
    if alder < 18:
        print("Ingen adgang.")
    elif 18 <= alder <= 65:
        print("Adgang tilladt.")
    else:
        print("Adgang begrænset.")

# Eksempel brug
tjek_adgang(15)
tjek_adgang(30)
tjek_adgang(70)

# Hvad der sker:
# - Vi bruger en if-elif-else struktur til at tjekke 'alder'.
# - Hvis 'alder' er mindre end 18, udskrives en besked om, at der ikke er adgang.
# - Hvis 'alder' er mellem 18 og 65 (inklusive), udskrives en besked om, at adgang er tilladt.
# - Hvis 'alder' er større end 65, udskrives en besked om, at adgang er begrænset.

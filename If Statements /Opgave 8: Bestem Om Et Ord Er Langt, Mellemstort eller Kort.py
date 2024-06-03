# Opgavebeskrivelse:
# Skriv et program, der bestemmer om et givet ord er langt, mellemstort eller kort og udskriver en passende besked.

def tjek_ord_længde(ord):
    længde = len(ord)
    if længde < 5:
        print(f"'{ord}' er et kort ord.")
    elif 5 <= længde <= 8:
        print(f"'{ord}' er et mellemstort ord.")
    else:
        print(f"'{ord}' er et langt ord.")

# Eksempel brug
tjek_ord_længde("kat")
tjek_ord_længde("husdyr")
tjek_ord_længde("programmering")

# Hvad der sker:
# - Vi bruger en if-elif-else struktur til at tjekke længden af 'ord'.
# - Hvis længden er mindre end 5, udskrives en besked om, at det er et kort ord.
# - Hvis længden er mellem 5 og 8 (inklusive), udskrives en besked om, at det er et mellemstort ord.
# - Hvis længden er større end 8, udskrives en besked om, at det er et langt ord.

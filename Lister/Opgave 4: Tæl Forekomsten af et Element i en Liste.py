def tæl_forekomst(liste, element):
    # Brug count() til at tælle forekomsten af elementet i listen
    return liste.count(element)

# Eksempel brug
min_liste = [1, 2, 3, 4, 2, 2, 5]
element = 2
print(f"Elementet {element} forekommer {tæl_forekomst(min_liste, element)} gange i listen.")

# Hvad der sker:
# - liste.count(element) tæller antallet af gange 'element' forekommer i listen 'liste'.
# - Vi returnerer antallet af forekomster.
# - Vi udskriver antallet af forekomster ved at kalde tæl_forekomst() funktionen med 'min_liste' og 'element' som argumenter.
# - Funktionen returnerer antallet af forekomster, som vi udskriver.
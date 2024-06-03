def omvendt_liste(liste):
    # Brug liste[::-1] til at omvende listen
    return liste[::-1]

# Eksempel brug
min_liste = [1, 2, 3, 4, 5]
print(f"Omvendt liste: {omvendt_liste(min_liste)}")

# Hvad der sker:
# - liste[::-1] skaber en ny liste, som er den omvendte version af 'liste'.
# - Vi returnerer den omvendte liste.
# - Vi udskriver den omvendte liste ved at kalde omvendt_liste() funktionen med 'min_liste' som argument.
# - Funktionen returnerer den omvendte liste, som vi udskriver.
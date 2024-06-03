def sorter_liste(liste):
    # Brug sorted() til at sortere listen
    return sorted(liste)

# Eksempel brug
min_liste = [5, 2, 9, 1, 7, 3]
print(f"Sorterede liste: {sorter_liste(min_liste)}")

# Hvad der sker:
# - sorted(liste) returnerer en ny liste, hvor elementerne i 'liste' er sorteret i stigende rækkefølge.
# - Vi returnerer den sorterede liste.
# - Vi udskriver den sorterede liste ved at kalde sorter_liste() funktionen med 'min_liste' som argument.
# - Funktionen returnerer den sorterede liste, som vi udskriver.
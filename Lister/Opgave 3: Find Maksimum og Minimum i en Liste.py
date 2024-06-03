def find_max_min(liste):
    # Brug max() til at finde det største tal og min() til at finde det mindste tal
    return max(liste), min(liste)

# Eksempel brug
min_liste = [5, 2, 9, 1, 7, 3]
maks, min = find_max_min(min_liste)
print(f"Det største tal er: {maks}")
print(f"Det mindste tal er: {min}")

# Hvad der sker:
# - max(liste) finder det største tal i listen 'liste'.
# - min(liste) finder det mindste tal i listen 'liste'.
# - Vi returnerer både det største og mindste tal.
# - Vi udskriver de fundne værdier ved at kalde find_max_min() funktionen med 'min_liste' som argument.
# - Funktionen returnerer både det største og mindste tal, som vi udskriver.
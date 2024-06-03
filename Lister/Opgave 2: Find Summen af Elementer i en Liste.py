def find_sum(liste):
    # Brug sum() til at beregne summen af listen
    return sum(liste)

# Eksempel brug
min_liste = [1, 2, 3, 4, 5]
print(f"Summen af listen er: {find_sum(min_liste)}")

# Hvad der sker:
# - sum(liste) beregner summen af alle elementerne i listen 'liste'.
# - Vi returnerer summen af listen.
# - Vi udskriver summen af listen ved at kalde find_sum() funktionen med 'min_liste' som argument.
# - Funktionen returnerer summen af listen, som vi udskriver.
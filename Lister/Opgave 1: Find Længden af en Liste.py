def find_længde(liste):
    # Brug len() til at finde længden af listen
    return len(liste)

# Eksempel brug
min_liste = [1, 2, 3, 4, 5]
print(f"Længden af listen er: {find_længde(min_liste)}")

# Hvad der sker:
# - len(liste) beregner antallet af elementer i listen 'liste'.
# - Vi returnerer længden af listen.
# - Vi udskriver længden af listen ved at kalde find_længde() funktionen med 'min_liste' som argument.
# - Funktionen returnerer længden af listen, som vi udskriver.
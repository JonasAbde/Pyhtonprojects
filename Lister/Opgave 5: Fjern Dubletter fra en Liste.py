def fjern_dubletter(liste):
    # Brug set() til at fjerne dubletter og konverter tilbage til liste
    return list(set(liste))

# Eksempel brug
min_liste = [1, 2, 3, 4, 2, 2, 5]
print(f"Liste uden dubletter: {fjern_dubletter(min_liste)}")

# Hvad der sker:
# - set(liste) konverterer listen 'liste' til et sæt, som automatisk fjerner dubletter.
# - Vi konverterer sættet tilbage til en liste ved hjælp af list().
# - Vi returnerer listen uden dubletter.
# - Vi udskriver listen uden dubletter ved at kalde fjern_dubletter() funktionen med 'min_liste' som argument.
# - Funktionen returnerer listen uden dubletter, som vi udskriver.
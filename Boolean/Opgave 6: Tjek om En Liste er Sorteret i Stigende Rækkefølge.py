# Opgavebeskrivelse:
# Skriv et program, der tjekker om en liste er sorteret i stigende rækkefølge og returnerer True, hvis den er, og False, hvis den ikke er.

def er_sorteret(liste):
    return all(liste[i] <= liste[i + 1] for i in range(len(liste) - 1))

# Eksempel brug
min_liste = [1, 2, 3, 4, 5]
print(f"Er listen sorteret i stigende rækkefølge? {er_sorteret(min_liste)}")

# Hvad der sker:
# - all(liste[i] <= liste[i + 1] for i in range(len(liste) - 1)) returnerer True, hvis alle elementerne i listen er i stigende rækkefølge, ellers returnerer det False.
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde er_sorteret() funktionen med 'min_liste' som argument.

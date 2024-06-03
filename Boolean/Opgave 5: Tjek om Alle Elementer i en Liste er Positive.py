# Opgavebeskrivelse:
# Skriv et program, der tjekker om alle elementer i en liste er positive og returnerer True, hvis de er, og False, hvis de ikke er.

def alle_positive(liste):
    return all(element > 0 for element in liste)

# Eksempel brug
min_liste = [1, 2, 3, 4, 5]
print(f"Er alle elementer i listen positive? {alle_positive(min_liste)}")

# Hvad der sker:
# - all(element > 0 for element in liste) returnerer True, hvis alle elementerne i listen er positive, ellers returnerer det False.
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde alle_positive() funktionen med 'min_liste' som argument.

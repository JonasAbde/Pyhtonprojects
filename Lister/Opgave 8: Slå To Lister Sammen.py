def slå_sammen(liste1, liste2):
    # Brug + operatoren til at slå de to lister sammen
    return liste1 + liste2

# Eksempel brug
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print(f"Sammenslået liste: {slå_sammen(liste1, liste2)}")

# Hvad der sker:
# - liste1 + liste2 skaber en ny liste, som er sammensat af elementerne i 'liste1' og 'liste2'.
# - Vi returnerer den sammenslåede liste.
# - Vi udskriver den sammenslåede liste ved at kalde slå_sammen() funktionen med 'liste1' og 'liste2' som argumenter.
# - Funktionen returnerer den sammenslåede liste, som vi udskriver.
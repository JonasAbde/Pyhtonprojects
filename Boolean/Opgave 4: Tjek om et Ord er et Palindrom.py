# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet ord er et palindrom og returnerer True, hvis det er, og False, hvis det ikke er.

def er_palindrom(ord):
    return ord == ord[::-1]

# Eksempel brug
ord = "radar"
print(f"Er '{ord}' et palindrom? {er_palindrom(ord)}")

# Hvad der sker:
# - ord == ord[::-1] tjekker, om ordet er det samme, når det læses baglæns.
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde er_palindrom() funktionen med 'ord' som argument.

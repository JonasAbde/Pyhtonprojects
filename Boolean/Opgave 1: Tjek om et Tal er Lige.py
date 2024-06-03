# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet tal er lige og returnerer True, hvis det er, og False, hvis det ikke er.

def er_lige(tal):
    return tal % 2 == 0

# Eksempel brug
tal = 4
print(f"Er {tal} lige? {er_lige(tal)}")

# Hvad der sker:
# - tal % 2 == 0 returnerer True, hvis 'tal' er lige, ellers returnerer det False.
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde er_lige() funktionen med 'tal' som argument.

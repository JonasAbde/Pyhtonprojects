# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet tal er positivt og returnerer True, hvis det er, og False, hvis det ikke er.

def er_positiv(tal):
    return tal > 0

# Eksempel brug
tal = 5
print(f"Er {tal} positivt? {er_positiv(tal)}")

# Hvad der sker:
# - tal > 0 returnerer True, hvis 'tal' er større end 0, ellers returnerer det False.
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde er_positiv() funktionen med 'tal' som argument.

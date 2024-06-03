# Opgavebeskrivelse:
# Skriv et program, der tjekker om to strenge er anagrammer af hinanden og returnerer True, hvis de er, og False, hvis de ikke er.

def er_anagrammer(streng1, streng2):
    return sorted(streng1) == sorted(streng2)

# Eksempel brug
streng1 = "listen"
streng2 = "silent"
print(f"Er '{streng1}' og '{streng2}' anagrammer? {er_anagrammer(streng1, streng2)}")

# Hvad der sker:
# - sorted(streng1) sorterer bogstaverne i 'streng1'.
# - sorted(streng2) sorterer bogstaverne i 'streng2'.
# - Vi sammenligner de sorterede lister af bogstaver for at tjekke, om de er ens.
# - Vi returnerer resultatet af denne booleanske sammenligning.
# - Vi udskriver resultatet ved at kalde er_anagrammer() funktionen med 'streng1' og 'streng2' som argumenter.

# Opgavebeskrivelse:
# Skriv et program, der tjekker om et givet tal er et primtal og returnerer True, hvis det er, og False, hvis det ikke er.

def er_primtal(tal):
    if tal <= 1:
        return False
    for i in range(2, int(tal**0.5) + 1):
        if tal % i == 0:
            return False
    return True

# Eksempel brug
tal = 7
print(f"Er {tal} et primtal? {er_primtal(tal)}")

# Hvad der sker:
# - Hvis 'tal' er mindre end eller lig med 1, returnerer vi False.
# - Vi itererer fra 2 til kvadratroden af 'tal' for at tjekke, om 'tal' har nogen divisorer.
# - Hvis 'tal' har en divisor, returnerer vi False.
# - Hvis 'tal' ikke har nogen divisorer, returnerer vi True.
# - Vi udskriver resultatet ved at kalde er_primtal() funktionen med 'tal' som argument.

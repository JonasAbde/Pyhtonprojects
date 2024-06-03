# Opgavebeskrivelse:
# Skriv et program, der bruger en for-løkke til at beregne faktorialet af et givet tal.

def beregn_faktorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

# Eksempel brug
tal = 5
print(f"Faktorialet af {tal} er: {beregn_faktorial(tal)}")

# Hvad der sker:
# - Vi initialiserer variablen 'faktorial' til 1.
# - for i in range(1, n + 1) itererer gennem tallene fra 1 til 'n'.
# - faktorial *= i multiplicerer 'faktorial' med 'i' for hver iteration.
# - Vi returnerer den beregnede faktorial.
# - Vi udskriver resultatet ved at kalde beregn_faktorial() funktionen med 'tal' som argument.

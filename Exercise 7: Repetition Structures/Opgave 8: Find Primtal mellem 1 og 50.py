# Opgavebeskrivelse:
# Skriv et program, der bruger en for-løkke til at finde alle primtal mellem 1 og 50.

def er_primtal(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Primtal mellem 1 og 50:")
for i in range(1, 51):
    if er_primtal(i):
        print(i)

# Hvad der sker:
# - er_primtal(n) funktionen tjekker, om 'n' er et primtal.
# - Hvis 'n' er mindre end eller lig med 1, returnerer vi False.
# - Vi itererer fra 2 til kvadratroden af 'n' for at tjekke, om 'n' har nogen divisorer.
# - Hvis 'n' har en divisor, returnerer vi False.
# - Hvis 'n' ikke har nogen divisorer, returnerer vi True.
# - for i in range(1, 51) itererer gennem tallene fra 1 til 50.
# - if er_primtal(i) tjekker, om 'i' er et primtal, og udskriver det, hvis det er.

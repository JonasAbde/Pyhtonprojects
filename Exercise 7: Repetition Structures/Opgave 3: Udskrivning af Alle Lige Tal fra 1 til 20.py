# Opgavebeskrivelse:
# Skriv et program, der bruger en for-løkke til at udskrive alle lige tal fra 1 til 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Hvad der sker:
# - for i in range(1, 21) itererer gennem tallene fra 1 til 20.
# - if i % 2 == 0 tjekker, om 'i' er et lige tal.
# - print(i) udskriver værdien af 'i', hvis 'i' er lige.

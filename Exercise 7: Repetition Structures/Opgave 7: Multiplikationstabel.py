# Opgavebeskrivelse:
# Skriv et program, der bruger en indlejret for-løkke til at udskrive en multiplikationstabel fra 1 til 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()

# Hvad der sker:
# - for i in range(1, 11) itererer gennem tallene fra 1 til 10 (yderste løkke).
# - for j in range(1, 11) itererer gennem tallene fra 1 til 10 (indre løkke).
# - print(f"{i} * {j} = {i * j}") udskriver produktet af 'i' og 'j'.
# - print() udskriver en tom linje efter hver tabel for bedre læsbarhed.

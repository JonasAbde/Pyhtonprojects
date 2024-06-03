# Opgavebeskrivelse:
# Skriv et program, der bruger en for-løkke til at beregne summen af alle tal fra 1 til 100.

sum = 0
for i in range(1, 101):
    sum += i
print(f"Summen af tallene fra 1 til 100 er: {sum}")

# Hvad der sker:
# - Vi initialiserer variablen 'sum' til 0.
# - for i in range(1, 101) itererer gennem tallene fra 1 til 100.
# - sum += i lægger værdien af 'i' til 'sum' for hver iteration.
# - Efter løkken udskriver vi den samlede sum.

# Opgavebeskrivelse:
# Skriv et program, der bruger en for-løkke til at udskrive de første 10 tal i Fibonacci-serien.

fib = [0, 1]
for i in range(2, 10):
    næste_tal = fib[i - 1] + fib[i - 2]
    fib.append(næste_tal)

print("De første 10 tal i Fibonacci-serien er:")
for nummer in fib:
    print(nummer)

# Hvad der sker:
# - Vi initialiserer listen 'fib' med de første to tal i Fibonacci-serien (0 og 1).
# - for i in range(2, 10) itererer gennem tallene fra 2 til 9.
# - næste_tal = fib[i - 1] + fib[i - 2] beregner det næste tal i serien.
# - fib.append(næste_tal) tilføjer det næste tal til listen.
# - Vi udskriver alle tal i listen 'fib'.

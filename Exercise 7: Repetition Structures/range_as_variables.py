# Exercise - Range as variables

# Bed brugeren om en startværdi
start = int(input("Indtast startværdi: "))

# Bed brugeren om en slutværdi
end = int(input("Indtast slutværdi: "))

# Bed brugeren om en trinværdi
step = int(input("Indtast trinværdi: "))

# Brug en for-loop med range til at udskrive tallene fra start til slut i trin
print(f"\nTallene fra {start} til {end} i trin af {step}:")
for i in range(start, end, step):
    print(i)

# Spørg brugeren om antallet af karakterer
antal_karakterer = int(input("Indtast antallet af karakterer, du vil beregne gennemsnittet for:"))

sum_karakterer = 0

# Opret en loop for at bede om karakterer
for i in range(antal_karakterer):
    # Brugeren indtaster en karakter
    karakter = float(input(f"Indtast karakter {i + 1}: "))
    # karakteren lægges til summen
    sum_karakterer += karakter

# Beregn gennemsnittet
gennemsnit = sum_karakterer / antal_karakterer

if gennemsnit < 2:
    print("så har du desværre dumbet")  # En motiverende besked

# gennemsnitlige karaktergennemsnit
print(f"Gennemsnittet af de indtastede karakterer er: {gennemsnit}")

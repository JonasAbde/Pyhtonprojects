# Øvelse - while loop

# Den korrekte adgangskode
korrekt_adgangskode = "hemmelig"

# Bed brugeren om en adgangskode
bruger_adgangskode = input("Indtast adgangskode: ")

# Brug en while-løkke til at fortsætte med at bede om adgangskoden, indtil den er korrekt
while bruger_adgangskode != korrekt_adgangskode:
    print("Forkert adgangskode. Prøv igen.")
    bruger_adgangskode = input("Indtast adgangskode: ")

# Når den korrekte adgangskode er indtastet
print("Adgangskode korrekt! Adgang givet.")

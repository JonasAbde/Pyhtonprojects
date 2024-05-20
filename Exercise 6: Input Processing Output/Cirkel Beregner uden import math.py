#Skriv et program der spørger brugeren om en radius på en cirkel.

#Programmet skal derefter beregne og udskrive arealet of omkredsen af cirklen.

#Brug πr^2  til udregning af arealet

#Brug 2πr for udregning af omkredsen.

# Definerer pi-værdien
pi = 3.14159

# Spørg brugeren om radius på en cirkel
radius = float(input("Indtast radius på en cirkel: "))

# Beregner arealet af cirklen
areal = pi * radius ** 2

# Beregner omkredsen af cirklen
omkreds = 2 * pi * radius

# Udskriver arealet og omkredsen af cirklen
print(f"Arealet af cirklen er: {areal:.2f}")
print(f"Omkredsen af cirklen er: {omkreds:.2f}")
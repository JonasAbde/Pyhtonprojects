"""Skriv en betingelse, der tjekker om variablen number er positiv,
og samtidigt enten ikke er delelig med 2 eller ikke er delelig med 3."""


number = input(int("indtast tal"))  # Eksempelværdi

if number > 0 and (number % 2 != 0 or number % 3 != 0):
    print(f"{number} er positiv og ikke delelig enten med 2 eller med 3.")
else:
    print(f"{number} er ikke positiv eller er delelig både med 2 og med 3.")

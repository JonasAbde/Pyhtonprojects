import random

# Opgave 1: Funktion 'shout'
def shout(message):
    """
    Accepterer en streng og viser den i store bogstaver med et udråbstegn tilføjet i slutningen.

    Args:
    message (str): Strengen, der skal vises.
    """
    print(message.upper() + '!')

# Eksempel på funktionskald for 'shout'
shout("hej")

# Opgave 2: Kald af funktionen 'show_value'
def show_value(quantity):
    """
    Viser den givne værdi.

    Args:
    quantity (int): Værdien, der skal vises.
    """
    print(quantity)

# Kald af funktionen 'show_value' med 12 som argument
show_value(12)

# Opgave 3: Funktion 'my_function(a, b, c)'
def my_function(a, b, c):
    """
    Eksempel funktion med tre parametre.

    Args:
    a, b, c: De værdier, der passerer til funktionens parametre.
    """
    print(f"a: {a}, b: {b}, c: {c}")

# Kald af funktionen 'my_function'
my_function(3, 2, 1)

# Opgave 4: Generering af tilfældigt tal
# Generer et tilfældigt tal i intervallet 1-100 og tildel det til variablen rand
rand = random.randint(1, 100)
print(f"Tilfældigt tal: {rand}")

# Opgave 5: Funktion 'times_ten'
def times_ten(number):
    """
    Accepterer et tal og returnerer det ganget med 10.

    Args:
    number (int or float): Tallet, der skal ganges med 10.

    Returns:
    int or float: Resultatet af tallet ganget med 10.
    """
    return number * 10

# Eksempel på funktionskald for 'times_ten'
result = times_ten(5)
print(f"5 gange 10 er: {result}")  # Udskriver 50

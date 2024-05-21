import random

def odd_even_counter():
    """
    Generer 100 tilfældige tal og hold styr på, hvor mange af dem der er lige og ulige.
    """
    even_count = 0
    odd_count = 0

    for _ in range(100):
        number = random.randint(1, 100)
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Vis resultaterne
    print(f"Antal lige tal: {even_count}")
    print(f"Antal ulige tal: {odd_count}")

# Kør programmet
odd_even_counter()

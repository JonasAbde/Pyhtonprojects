def max(a, b):
    """
    Returner den største af to heltalsværdier.

    Args:
    a (int): Den første heltalsværdi.
    b (int): Den anden heltalsværdi.

    Returns:
    int: Den største af de to værdier.
    """
    if a > b:
        return a
    else:
        return b

# Hovedprogram
def main():
    """
    Hovedprogram der beder brugeren om at indtaste to heltalsværdier og viser den største af dem.
    """
    # Bed brugeren om at indtaste to heltalsværdier
    num1 = int(input("Indtast det første heltal: "))
    num2 = int(input("Indtast det andet heltal: "))

    # Brug max-funktionen til at finde den største værdi
    largest_value = max(num1, num2)

    # Vis den største værdi
    print(f"Den største værdi af {num1} og {num2} er {largest_value}")

# Kald hovedprogrammet
main()

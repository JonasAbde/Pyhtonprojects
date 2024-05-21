import random

def parallel_resistance(R1, R2):
    """
    Beregn og returner modstanden af to modstande i parallel.

    Args:
    R1 (float): Modstanden af den første modstand.
    R2 (float): Modstanden af den anden modstand.

    Returns:
    float: Den samlede parallel modstand.
    """
    return (R1 * R2) / (R1 + R2)

def random_number():
    """
    Returner et tilfældigt tal mellem 1 og 100.

    Returns:
    int: Et tilfældigt tal mellem 1 og 100.
    """
    return random.randint(1, 100)

# Eksempler på funktionskald
resistance = parallel_resistance(100, 200)
print(f"Parallel modstand: {resistance} ohm")

rand_num = random_number()
print(f"Tilfældigt tal: {rand_num}")

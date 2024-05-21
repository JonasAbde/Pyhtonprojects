def parallel_resistance(R1, R2):
    """
    Beregn og returner modstanden af to modstande i parallel.

    Args:
    R1 (float): Modstanden af den første modstand.
    R2 (float): Modstanden af den anden modstand.

    Returns:
    float: Den samlede parallel modstand.
    """
    if R1 == 0 or R2 == 0:
        return 0
    return (R1 * R2) / (R1 + R2)

# Eksempler på funktionskald
resistance = parallel_resistance(100, 200)
print(f"Parallel modstand: {resistance} ohm")

resistance = parallel_resistance(50, 100)
print(f"Parallel modstand: {resistance} ohm")

resistance = parallel_resistance(0, 100)  # Edge case: one resistor is zero
print(f"Parallel modstand (med en modstand på 0 ohm): {resistance} ohm")

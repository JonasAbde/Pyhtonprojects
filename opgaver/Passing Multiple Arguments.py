def calculate_average(num1, num2, num3):
    """
    Beregn og print gennemsnittet af tre tal.

    Args:
    num1 (float): Det første tal.
    num2 (float): Det andet tal.
    num3 (float): Det tredje tal.
    """
    average = (num1 + num2 + num3) / 3
    print(f"Gennemsnittet af {num1}, {num2} og {num3} er {average}")

# Eksempel på funktionskald
calculate_average(10, 20, 30)

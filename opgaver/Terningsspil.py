import random


# Modul funktioner

def roll_dice():
    """
    Returnerer et tilfældigt tal mellem 1 og 6 for at simulere et terningekast.
    """
    return random.randint(1, 6)


def print_dice(value):
    """
    Udskriver en grafisk afbildning af terningen baseret på værdien.
    """
    if value == 1:
        print("""
        -----
        |   |
        | * |
        |   |
        -----
        """)
    elif value == 2:
        print("""
        -----
        |*  |
        |   |
        |  *|
        -----
        """)
    elif value == 3:
        print("""
        -----
        |*  |
        | * |
        |  *|
        -----
        """)
    elif value == 4:
        print("""
        -----
        |* *|
        |   |
        |* *|
        -----
        """)
    elif value == 5:
        print("""
        -----
        |* *|
        | * |
        |* *|
        -----
        """)
    elif value == 6:
        print("""
        -----
        |* *|
        |* *|
        |* *|
        -----
        """)


# Hovedprogram

def main():
    while True:
        print("\nMenu")
        print("1. Kast terningerne")
        print("2. Afslut")

        choice = input("Vælg en mulighed (1-2): ")

        if choice == '2':
            print("Afslutter programmet.")
            break

        if choice == '1':
            player_roll = roll_dice()
            computer_roll = roll_dice()

            print("Du slog:")
            print_dice(player_roll)

            print("Computeren slog:")
            print_dice(computer_roll)

            if player_roll > computer_roll:
                print("Du har vundet!")
            elif player_roll < computer_roll:
                print("Computeren har vundet!")
            else:
                print("Det er uafgjort!")
        else:
            print("Ugyldigt valg. Prøv igen.")


if __name__ == "__main__":
    main()

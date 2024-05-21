# Regnemaskine Modul

def add(a, b):
    """
    Returnerer summen af to tal.
    """
    return a + b

def subtract(a, b):
    """
    Returnerer forskellen mellem to tal.
    """
    return a - b

def multiply(a, b):
    """
    Returnerer produktet af to tal.
    """
    return a * b

def divide(a, b):
    """
    Returnerer kvotienten af to tal.
    """
    if b == 0:
        return "Fejl: Division med nul"
    return a / b

# Hovedprogram

def main():
    while True:
        print("\nRegnemaskine Menu")
        print("1. Addition (+)")
        print("2. Subtraktion (-)")
        print("3. Multiplikation (*)")
        print("4. Division (/)")
        print("5. Afslut")

        choice = input("Vælg en operation (1-5): ")

        if choice == '5':
            print("Afslutter programmet.")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Indtast det første tal: "))
            num2 = float(input("Indtast det andet tal: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            print(f"Resultatet er: {result}")
        else:
            print("Ugyldigt valg. Prøv igen.")

if __name__ == "__main__":
    main()

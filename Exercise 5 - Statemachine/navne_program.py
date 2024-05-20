def start():
    print("Start")
    return indtast_antal_navne()


def indtast_antal_navne():
    print("\nIndtast antal navne og navnene:")
    antal = int(input("Hvor mange navne vil du indtaste? "))
    navne = []
    for _ in range(antal):
        navn = input("Indtast et navn: ")
        navne.append(navn)

    # Opretter filen navne.txt og skriver navnene til filen
    with open("navne.txt", "w") as f:
        for navn in navne:
            f.write(navn + "\n")

    return menu()


def menu():
    while True:
        print("\nMenu:")
        print("1) Udskriv navne")
        print("2) Nye fil med nye navne")
        print("3) Tilføj flere navne til eksisterende fil")
        print("4) Afslut programmet")
        valg = input("Vælg en mulighed (1, 2, 3, 4): ")

        if valg == '1':
            skriv_navne_ud()
        elif valg == '2':
            indtast_antal_navne()
        elif valg == '3':
            tilfoj_flere_navne()
        elif valg == '4':
            afslut()
            break
        else:
            print("Ugyldigt valg. Prøv igen.")


def skriv_navne_ud():
    try:
        with open("navne.txt", "r") as f:
            navne = f.readlines()
            print("\nNavne i filen:")
            for navn in navne:
                print(navn.strip())
    except FileNotFoundError:
        print("\nFilen navne.txt blev ikke fundet.")


def tilfoj_flere_navne():
    with open("navne.txt", "a") as f:
        antal = int(input("Hvor mange navne vil du tilføje? "))
        for _ in range(antal):
            navn = input("Indtast et navn: ")
            f.write(navn + "\n")


def afslut():
    print("\nProgrammet afsluttes.")


if __name__ == "__main__":
    start()

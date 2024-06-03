def state1_list():
    tal = []
    print("Indtast 10 tal:")
    for _ in range(10):
        tal.append(int(input(f"Indtast tal {_ + 1}: ")))
    return tal


def state2_menu(tal):
    print("\nMenu:")
    print("1) Indtast flere tal")
    print("2) Find max og min")
    print("3) Sorter tallene")
    valg = input("Vælg en mulighed (1, 2, eller 3): ")
    if valg == '1':
        state3_append(tal)
    elif valg == '2':
        state4_maxOGmin(tal)
    elif valg == '3':
        state5_sort(tal)
    else:
        print("Ugyldigt valg. Prøv igen.")
        state2_menu(tal)


def state3_append(tal):
    print("Indtast yderligere tal (skriv 'færdig' for at afslutte):")
    while True:
        nummer = input("Indtast et tal: ")
        if nummer.lower() == 'færdig':
            break
        try:
            tal.append(float(nummer))
        except ValueError:
            print("Ugyldigt input. Indtast et gyldigt tal.")
    state6_antal_karakter(tal)
    state2_menu(tal)



def state4_maxOGmin(tal):
    print(f"Det maksimale tal er: {max(tal)}")
    print(f"Det minimale tal er: {min(tal)}")
    state2_menu(tal)


def state5_sort(tal):
    print(f"Den sorterede liste er: {sorted(tal)}")
    state2_menu(tal)


def state6_antal_karakter(tal):
    print(f"Det totale antal elementer i listen er: {len(tal)}")
    state2_menu(tal)


def main():
    tal = state1_list()
    state2_menu(tal)

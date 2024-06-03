import random


def state1():
    tal = [random.randint(0, 10) for _ in range(0, 20)]
    return tal


def state2(tal):
    # Sorter tallene i to nye lister: 0-4 og 5-10
    liste_0_4 = [num for num in tal if num >= 0 and num <= 4]
    liste_5_10 = [num for num in tal if num >= 5 and num <= 10]
    return liste_0_4, liste_5_10


def state3(liste_0_4, liste_5_10):
    print("Liste med tal mellem 0 og 4:", liste_0_4)
    print("Liste med tal mellem 5 og 10:", liste_5_10)


def main():
    tal = state1()
    liste_0_4, liste_5_10 = state2(tal)
    state3(liste_0_4, liste_5_10)


if __name__ == "__main__":
    main()

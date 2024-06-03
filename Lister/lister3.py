import random


def main():
    tal_liste = []  # Opretter list
    for taller in range(20):  # Generer 20 tilfældige tal.
        tal = random.randrange(0, 10, 1)
        tal_liste.append(tal)  # Tilføjer tal til listen(tal_liste)
        print(tal)
    print(tal_liste)
    sortere(tal_liste)  # overføre liste til sort funktionen.


def sortere(tal_liste):
    tal_04 = []  # Ny liste til tal mellem 0 og 4.
    tal_510 = []  # Ny liste til tal mellem 5 og 10.
    for tall in range(20):
        if tal_liste[tall] < 5:  # Er tallet mindre end 5?
            tal_04.append(tal_liste[tall])  # Læg tal over i tal_04.
        elif tal_liste[tall] > 5:  # Er tallet større end 5
            tal_510.append(tal_liste[tall])  # Læg tal over i tal_510.
        else:
            tal_510.append(tal_liste[tall])  # Er tallet større end 5
    print(tal_04)
    print(tal_510)
    tal_print(tal_04, tal_510)  # Overføre lister til tal_print.


def tal_print(tal_04, tal_510):
    print(tal_04)
    print(tal_510)
    print(f"Nu udskrives tallene fra 0 til 4: {tal_04}")
    print(f"Nu udskrives tallene fra 5 til 10: {tal_510}")


main()

import random

# Generer en liste med 20 tilfældige tal mellem 0 og 100
liste = [random.randint(0, 100) for _ in range(20)]


def menu():
    print(
        "1) Sortere listen og lægger i liste.txt\n"
        "2) Tæller antal karakter i listen og lægger i liste.txt \n"
        "3) Finder min og max i listen og ligger dem i liste.txt\n"
        "4) Stop"
    )
    valg = int(input("indtast dit valg her: "))  # Korrekt brug af input
    if valg == 1:
        sortere()
    elif valg == 2:
        taller_karakter()
    elif valg == 3:
        minOGmax()
    elif valg == 4:
        exit()
    else:
        print("prøv igen")
        menu()

def sortere():
    liste.sort()
    file("Sorteret liste: ", liste)
    menu()

def taller_karakter():
    antal_karakterer = len(liste)
    file("Antal karakterer i listen: ", antal_karakterer)
    menu()

def minOGmax():
    minimum = min(liste)
    maksimum = max(liste)
    file("Min og max vaerdier", f"Min: {minimum}, Max: {maksimum}")
    menu()

def file(beskrivelse, liste):
    with open("liste.txt", "a") as f:  # 'a' for append mode
        f.write(f"{beskrivelse}\n")
        f.write(f"{str(liste)}\n")
        f.write("\n")


menu()
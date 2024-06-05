import random

liste2 = ["Emma", "Alma", "Clara", "Freja", "Sofie", "Ella", "Ida", "Lily", "Anna", "Nora"]


def menu():
    print(
        "1) Sortere listen og lægger i liste2.txt\n"
        "2) Tæller antal navne i listen og lægger i liste2.txt\n"
        "3) Finder alfabetisk første og sidste navn i listen og ligger dem i liste2.txt\n"
        "4) Tilføj et navn til listen\n"
        "5) Stop"
    )
    valg = int(input("indtast dit valg her: "))  # Korrekt brug af input
    if valg == 1:
        sortere()
    elif valg == 2:
        tæller_navne()
    elif valg == 3:
        første_og_sidste()
    elif valg == 4:
        tilføj_navn()
    elif valg == 5:
        exit()
    else:
        print("prøv igen")
        menu()


def sortere():
    liste2.sort()
    file("Sorteret liste: ", liste2)
    menu()


def tæller_navne():
    antal_navne = len(liste2)
    file("Antal navne i listen: ", antal_navne)
    menu()


def første_og_sidste():
    første = min(liste2)
    sidste = max(liste2)
    file("Alfabetisk første og sidste navn", f"Første: {første}, Sidste: {sidste}")
    menu()


def tilføj_navn():
    navn = input("Indtast et navn, du vil tilføje til listen: ")
    liste2.append(navn)
    file(f"Tilføjet navn: {navn}", liste2)
    menu()


def file(beskrivelse, liste):
    with open("liste2.txt", "a") as f:  # 'a' for append mode
        f.write(f"{beskrivelse}\n")
        f.write(f"{str(liste)}\n")
        f.write("\n")
        f.close()

import random

# State: Talgen()
def talgen():
    # Generer en liste med 10 tilfældige tal mellem 0 og 100
    tal_100 = [random.randint(0, 100) for _ in range(10)]
    return tal_100

# State: adder()
def adder(tal_100):
    # Beregn summen af tallene i listen
    summen = sum(tal_100)
    print(f"Summen af listen: {summen}")
    # Tilføj summen til listen
    tal_100.append(summen)
    return tal_100

# State: sorter_list()
def sorter_list(tal_100):
    # Sorter listen i stigende rækkefølge
    tal_100.sort()
    print(f"Sorteret liste: {tal_100}")
    return tal_100

# State: list_to_fil()
def list_to_fil(tal_100):
    # Skriv listen til en fil med navnet 'list100.txt'
    with open('../opgave file input/list100.txt', 'w') as file:
        for item in tal_100:
            file.write(f"{item}\n")
    print("Listen er skrevet til list100.txt")

# Hovedfunktion til at udføre staterne
def main():
    # Generer 10 tilfældige tal
    tal_100 = talgen()
    # Læg tallene sammen og tilføj summen til listen
    tal_100 = adder(tal_100)
    # Sorter listen
    tal_100 = sorter_list(tal_100)
    # Skriv listen til en fil
    list_to_fil(tal_100)

if __name__ == "__main__":
    main()


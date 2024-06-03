import random

# Definer tilstands funktioner
def talgen():
    print("Tilstand: talgen()")
    tal_100 = [random.randint(0, 100) for _ in range(10)]
    return tal_100, udskr50_100

def udskr50_100(tal_100):
    print("Tilstand: udskr50_100()")
    filtrerede_tal = [num for num in tal_100 if 50 <= num <= 100]
    print(f"Tal mellem 50 og 100: {filtrerede_tal}")
    return tal_100, max_min_sum

def max_min_sum(tal_100):
    print("Tilstand: max_min_sum()")
    max_tal = max(tal_100)
    min_tal = min(tal_100)
    sum_max_min = max_tal + min_tal
    tal_100.append(sum_max_min)
    print(f"Max tal: {max_tal}, Min tal: {min_tal}, Sum: {sum_max_min}")
    return tal_100, list_to_fil

def list_to_fil(tal_100):
    print("Tilstand: list_to_fil()")
    with open("list100.txt", "w") as fil:
        for num in tal_100:
            fil.write(f"{num}\n")
    print(f"Liste gemt til list100.txt: {tal_100}")
    return None

# Initialiser starttilstand
nuværende_tilstand = talgen
tal_100 = []

# Kør statemaskinen
while nuværende_tilstand:
    tal_100, nuværende_tilstand = nuværende_tilstand(tal_100)
print("Færdig med tilstande")


# Skriv en funktion, der tager en liste af tal som argument og returnerer det mindste tal i listen.
import random

def find_min_i_list(numbers):
    return min(numbers)

# Eksempel på kald af funktionen
tal_liste = [5, 3, 8, 2, 9, 1]
resultat = find_min_i_list(tal_liste)
print(f' den generede liste er: {tal_liste}')
print(f"Det mindste tal i listen er: {resultat}")


def find_min_in_list(numbers):
    return min(numbers)

# Genererer en liste af tilfældige tal
random_list = [random.randint(1, 100) for _ in range(10)]
print(f"Den genererede liste er: {random_list}")

resultat = find_min_in_list(random_list)
print(f"Det mindste tal i listen er: {resultat}")

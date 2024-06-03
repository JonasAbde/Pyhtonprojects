# Skriv en funktion, der tager et hel tal n som argument og
# returnerer en liste med kvadraterne af tallene fra 1 til n.

#eksempel 1

def Kvadrat(k):
    return k * k


for i in range(1, 11):
    print(Kvadrat(i))

#eksempel 2
def kvadrater_op_til_n(n):
    return [k * k for k in range(1, n + 1)]

# Eksempel på brug
n = 10
resultat = kvadrater_op_til_n(n)
print(f"Kvadraterne af tallene fra 1 til {n} er: {resultat}")
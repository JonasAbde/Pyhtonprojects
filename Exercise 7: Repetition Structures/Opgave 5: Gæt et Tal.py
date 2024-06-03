# Opgavebeskrivelse:
# Skriv et program, hvor brugeren skal gætte et tilfældigt valgt tal mellem 1 og 100.

import random

hemmeligt_tal = random.randint(1, 100)
gæt = None

while gæt != hemmeligt_tal:
    gæt = int(input("Gæt et tal mellem 1 og 100: "))
    if gæt < hemmeligt_tal:
        print("For lavt, prøv igen!")
    elif gæt > hemmeligt_tal:
        print("For højt, prøv igen!")
    else:
        print("Tillykke, du gættede rigtigt!")

# Hvad der sker:
# - Vi bruger random.randint(1, 100) til at generere et tilfældigt tal mellem 1 og 100.
# - Vi initialiserer variablen 'gæt' til None.
# - while gæt != hemmeligt_tal kører løkken, indtil brugeren gætter det hemmelige tal.
# - gæt = int(input("Gæt et tal mellem 1 og 100: ")) beder brugeren om at indtaste et gæt.
# - if gæt < hemmeligt_tal giver brugeren et hint, hvis gættet er for lavt.
# - elif gæt > hemmeligt_tal giver brugeren et hint, hvis gættet er for højt.
# - else udskriver en besked om, at gættet er korrekt, og stopper løkken.

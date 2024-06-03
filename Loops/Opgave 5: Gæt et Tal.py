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

#Program der skal kunne udregne strømmen igennem 2 modstande der paralelle og et antal modstande i serie.


def Paralelle():
    print("Indtast værdierne for de 2 modstande der paralelle?")
    modstande1 = float(input("1 modstand"))
    modstande2 = float(input("2 modstand"))
    modstande3 = modstande2*modstande1/(modstande1+modstande2)
    print(F"Erstatsnings modstand = {modstande3} [Ohm]")
    spaending = float(input("Indtast spændingen for kredsløbet"))
    Serie(spaending, modstande3)



def Serie(spaending, modstande):
    modstand_serie = int(input("Indtast værdien af modstande der i serie med de 2 paralelle?"))
    sum_modstand= modstand_serie+modstande
    print("""1) indtast en modstand mere i serie med den paralelle?
2) Beregn strømmen i kredsløbet""")
    valg = int(input())
    if valg == 1:
        Serie(spaending, sum_modstand)
    elif valg ==2:
        I(spaending,sum_modstand)



def I(spaending, sum_modstand):
    strøm = spaending/sum_modstand
    print(F"Strømmen i kredsløbet = {strøm} [A]")
    print(F"Spændingen i kredsløbet = {spaending} [V]")
    print(F"Modstanden i kredsløbet = {sum_modstand} [Ohm]")
    File(spaending, sum_modstand, strøm)
  
def File(spaending, sum_modstand, strøm):
    file = open("modst.txt", "a")
    file.write("\n")
    file.write(f"Modstanden i kredsloebet = {str(sum_modstand)} [Ohm]")
    file.write("\n")
    file.write(f"Spaendingen i kredsloebet = {str(spaending)} [V]")
    file.write("\n")
    file.write(f"Stroemmen i kredsloebet = {str(strøm)} [A]")
    file.close()


Paralelle()
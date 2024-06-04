#Progam til at beregne U,I og R

def Menu():
    print("""1) Udregn U
2) Udregn I
3) Udregn R
4) Stop""")
    valg = input("indtast valg? ")
    if valg == "1":
        I = float(input("Indtast strømværdien "))
        R = float(input("Indtast modstandsværdien"))
        Udregn_U(I, R)
    elif valg == "2":
        U = float(input("Indtast spændindingsværdien "))
        R = float(input("Indtast modstandsværdien"))
        Udregn_I(U, R)
    elif valg == "3":
        U = float(input("Indtast spændindingsværdien "))
        I = float(input("Indtast strømværdien "))
        Udregn_R(U, I)
    elif valg == "4":
        exit()
    else:
        print("Du har indtastet et ugyldigt valg")
        Menu()
def Udregn_U(R, I):
    print(F"U = R * I = {R*I}")
    y= R*I
    File(y)
    Menu()
def Udregn_I(U, R):
    print(F"I = U / R = {U/R}")
    y=U/R
    File(y)
    Menu()

def Udregn_R(U, I):
    print(F"R = U / I = {U/I}")
    y= U/I
    File(y)
    Menu()

def File(y):
    f = open("ohm.txt", "a")
    f.write(str(y))
    f.write("\n")
    f.close()
    return

Menu()
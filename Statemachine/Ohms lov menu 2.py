class OhmsLawStateMachine:
    def __init__(self):
        self.state = 'menu'
        self.U = None
        self.I = None
        self.R = None

    def transition(self, event):
        if event == '1':
            self.beregn_U()
        elif event == '2':
            self.beregn_I()
        elif event == '3':
            self.beregn_R()
        elif event == '4':
            self.state = 'stop'
        else:
            print("Ugyldigt valg, prøv igen.")
        if self.state != 'stop':
            self.state = 'menu'

    def beregn_U(self):
        self.I = float(input("Indtast strømstyrke (I): "))
        self.R = float(input("Indtast modstand (R): "))
        self.U = self.I * self.R
        print(f"Spænding (U) er: {self.U}")
        self.gem_beregning("U")

    def beregn_I(self):
        self.U = float(input("Indtast spænding (U): "))
        self.R = float(input("Indtast modstand (R): "))
        self.I = self.U / self.R
        print(f"Strømstyrke (I) er: {self.I}")
        self.gem_beregning("I")

    def beregn_R(self):
        self.U = float(input("Indtast spænding (U): "))
        self.I = float(input("Indtast strømstyrke (I): "))
        self.R = self.U / self.I
        print(f"Modstand (R) er: {self.R}")
        self.gem_beregning("R")

    def gem_beregning(self, beregningstype):
        try:
            with open("ohm.txt", "a") as fil:
                if beregningstype == "U":
                    fil.write(f"U = I * R = {self.I} * {self.R} = {self.U}\n")
                elif beregningstype == "I":
                    fil.write(f"I = U / R = {self.U} / {self.R} = {self.I}\n")
                elif beregningstype == "R":
                    fil.write(f"R = U / I = {self.U} / {self.I} = {self.R}\n")
            print("Beregning gemt i ohm.txt")
        except Exception as e:
            print(f"Der opstod en fejl ved skrivning til filen: {e}")

# Hovedprogram
sm = OhmsLawStateMachine()

while sm.state != 'stop':
    print("\nMenu:")
    print("1) Beregn U")
    print("2) Beregn I")
    print("3) Beregn R")
    print("4) Stop")
    valg = input("Vælg en mulighed: ")
    sm.transition(valg)

# Hvad der sker:
# - Klassen OhmsLawStateMachine håndterer tilstande og overgange mellem dem.
# - transition(event) metoden styrer overgange mellem tilstande baseret på brugerinput.
# - beregn_U(), beregn_I(), og beregn_R() metoderne håndterer beregninger og gemmer resultaterne.
# - gem_beregning(beregningstype) metoden gemmer beregninger i en fil og håndterer eventuelle fejl.
# - Hovedprogrammet præsenterer en menu for brugeren og håndterer brugerens valg indtil 'stop' vælges.

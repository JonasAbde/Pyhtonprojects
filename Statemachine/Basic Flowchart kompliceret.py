class CircuitStateMachine:
    def __init__(self):
        self.state = 'parallel'
        self.R1 = None
        self.R2 = None
        self.R3 = None
        self.V = None
        self.R_parallel = None
        self.R_total = None
        self.I = None

    def transition(self, event):
        if self.state == 'parallel':
            self.beregn_parallel()
        elif self.state == 'serie':
            if event == '1':
                self.tilføj_modstand_serie()
            elif event == '2':
                self.beregn_strøm()
        elif self.state == 'stop':
            print("Programmet afsluttes.")
        else:
            print("Ugyldig tilstand.")

    def beregn_parallel(self):
        self.R1 = float(input("Indtast værdi for R1: "))
        self.R2 = float(input("Indtast værdi for R2: "))
        self.V = float(input("Indtast værdi for V (spænding): "))
        self.R_parallel = 1 / ((1 / self.R1) + (1 / self.R2))
        print(f"Den samlede parallel modstand er: {self.R_parallel}")
        self.state = 'serie'

    def tilføj_modstand_serie(self):
        self.R3 = float(input("Indtast værdi for R3: "))
        self.R_total = self.R_parallel + self.R3
        print(f"Den samlede modstand i serie er: {self.R_total}")
        self.state = 'serie_menu'

    def beregn_strøm(self):
        self.I = self.V / self.R_total
        print(f"Strømmen (I) er: {self.I}")
        self.gem_beregning()
        self.state = 'stop'

    def gem_beregning(self):
        try:
            with open("modstand.txt", "a") as fil:
                fil.write(f"V = {self.V}, R_parallel = {self.R_parallel}, R_total = {self.R_total}, I = {self.I}\n")
            print("Beregning gemt i modstand.txt")
        except Exception as e:
            print(f"Der opstod en fejl ved skrivning til filen: {e}")

# Hovedprogram
sm = CircuitStateMachine()

while sm.state != 'stop':
    if sm.state == 'parallel':
        sm.transition(None)
    elif sm.state == 'serie':
        print("\nSerie Menu:")
        print("1) Tilføj en modstand i serie")
        print("2) Beregn strømmen")
        valg = input("Vælg en mulighed: ")
        sm.transition(valg)
    elif sm.state == 'serie_menu':
        print("Gå tilbage til serie beregning.")
        sm.transition('2')

# Hvad der sker:
# - Klassen CircuitStateMachine håndterer tilstande og overgange mellem dem.
# - transition(event) metoden styrer overgange mellem tilstande baseret på brugerinput.
# - beregn_parallel(), tilføj_modstand_serie(), og beregn_strøm() metoderne håndterer beregninger og opdaterer tilstanden.
# - gem_beregning() metoden gemmer beregninger i en fil og håndterer eventuelle fejl.
# - Hovedprogrammet præsenterer en menu for brugeren og håndterer brugerens valg indtil 'stop' vælges.

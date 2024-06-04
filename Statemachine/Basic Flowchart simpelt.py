class SimpleCircuitStateMachine:
    def __init__(self):
        self.state = 'parallel'
        self.R1 = None
        self.R2 = None
        self.R3 = None
        self.V = None
        self.R_total = None
        self.I = None

    def transition(self, event):
        if self.state == 'parallel':
            self.R1 = float(input("Indtast værdi for R1: "))
            self.R2 = float(input("Indtast værdi for R2: "))
            self.V = float(input("Indtast værdi for V (spænding): "))
            self.R_total = 1 / ((1 / self.R1) + (1 / self.R2))
            print(f"Den samlede parallel modstand er: {self.R_total}")
            self.state = 'serie'
        elif self.state == 'serie':
            self.R3 = float(input("Indtast værdi for R3: "))
            self.R_total += self.R3
            print(f"Den samlede modstand i serie er: {self.R_total}")
            self.I = self.V / self.R_total
            print(f"Strømmen (I) er: {self.I}")
            self.gem_beregning()
            self.state = 'stop'

    def gem_beregning(self):
        try:
            with open("modstand.txt", "a") as fil:
                fil.write(f"V = {self.V}, R_total = {self.R_total}, I = {self.I}\n")
            print("Beregning gemt i modstand.txt")
        except Exception as e:
            print(f"Der opstod en fejl ved skrivning til filen: {e}")

# Hovedprogram
sm = SimpleCircuitStateMachine()

while sm.state != 'stop':
    sm.transition(None)

# Hvad der sker:
# - Klassen SimpleCircuitStateMachine håndterer tilstande og overgange mellem dem.
# - transition(event) metoden styrer overgange mellem tilstande baseret på brugerinput.
# - Beregninger og filskrivning udføres direkte i transition metoden.
# - Hovedprogrammet håndterer overgangene indtil 'stop' tilstanden nås.

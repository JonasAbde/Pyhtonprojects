class NavneUdskriftTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.filename = 'navne.txt'
        self.names = []

    def transition(self, event):
        if self.state == 'start' and event == 'læs_fil':
            try:
                with open(self.filename, 'r') as file:
                    self.names = [line.strip() for line in file]
                print(f"Læste navne: {self.names}")
                self.state = 'læst'
            except FileNotFoundError:
                print(f"Fil {self.filename} blev ikke fundet.")
                self.state = 'fejl'
        elif self.state == 'læst' and event == 'udskriv_navne':
            print("Navne i filen:")
            for name in self.names:
                print(name)
            self.state = 'udskrevet'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = NavneUdskriftTilstandsmaskine()
sm.transition('læs_fil')
sm.transition('udskriv_navne')
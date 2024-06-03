class SletFilIndholdTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.filename = 'slet_indhold.txt'

    def transition(self, event):
        if self.state == 'start' and event == 'slet_indhold':
            open(self.filename, 'w').close()
            print(f"Indholdet af filen {self.filename} er slettet.")
            self.state = 'slettet'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = SletFilIndholdTilstandsmaskine()
sm.transition('slet_indhold')
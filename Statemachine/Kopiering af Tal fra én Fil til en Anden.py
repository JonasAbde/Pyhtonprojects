class KopiTalTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.input_file = 'tal.txt'
        self.output_file = 'kopi_tal.txt'
        self.numbers = []

    def transition(self, event):
        if self.state == 'start' and event == 'læs_fil':
            try:
                with open(self.input_file, 'r') as file:
                    self.numbers = [int(line.strip()) for line in file]
                print(f"Læste tal: {self.numbers}")
                self.state = 'læst'
            except FileNotFoundError:
                print(f"Fil {self.input_file} blev ikke fundet.")
                self.state = 'fejl'
        elif self.state == 'læst' and event == 'kopier_tal':
            with open(self.output_file, 'w') as file:
                for number in self.numbers:
                    file.write(f"{number}\n")
            print("Tallene er kopieret til kopi_tal.txt")
            self.state = 'kopieret'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = KopiTalTilstandsmaskine()
sm.transition('læs_fil')
sm.transition('kopier_tal')

class GennemsnitTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.input_file = 'numbers.txt'
        self.output_file = 'average.txt'
        self.numbers = []
        self.average = 0

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
        elif self.state == 'læst' and event == 'beregn_gennemsnit':
            if self.numbers:
                self.average = sum(self.numbers) / len(self.numbers)
                print(f"Beregnet gennemsnit: {self.average}")
                self.state = 'beregnet'
            else:
                print("Ingen tal at beregne gennemsnit af.")
                self.state = 'fejl'
        elif self.state == 'beregnet' and event == 'skriv_fil':
            with open(self.output_file, 'w') as file:
                file.write(f"Gennemsnit: {self.average}\n")
            print("Gennemsnittet er skrevet til average.txt")
            self.state = 'færdig'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = GennemsnitTilstandsmaskine()
sm.transition('læs_fil')
sm.transition('beregn_gennemsnit')
sm.transition('skriv_fil')

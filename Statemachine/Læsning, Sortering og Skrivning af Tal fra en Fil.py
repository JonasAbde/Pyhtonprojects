class SorteringTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.input_file = 'unsorted.txt'
        self.output_file = 'sorted.txt'
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
        elif self.state == 'læst' and event == 'sorter_tal':
            self.numbers.sort()
            print(f"Sorterede tal: {self.numbers}")
            self.state = 'sorteret'
        elif self.state == 'sorteret' and event == 'skriv_fil':
            with open(self.output_file, 'w') as file:
                for number in self.numbers:
                    file.write(f"{number}\n")
            print("Sorterede tal er skrevet til sorted.txt")
            self.state = 'færdig'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = SorteringTilstandsmaskine()
sm.transition('læs_fil')
sm.transition('sorter_tal')
sm.transition('skriv_fil')

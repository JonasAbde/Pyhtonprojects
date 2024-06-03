class FiltreringTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.input_file = 'input.txt'
        self.output_file = 'filtered.txt'
        self.numbers = []
        self.filtered_numbers = []

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
        elif self.state == 'læst' and event == 'filtrer_tal':
            self.filtered_numbers = [num for num in self.numbers if num > 50]
            print(f"Filtrerede tal (større end 50): {self.filtered_numbers}")
            self.state = 'filtreret'
        elif self.state == 'filtreret' and event == 'skriv_fil':
            with open(self.output_file, 'w') as file:
                for number in self.filtered_numbers:
                    file.write(f"{number}\n")
            print("Filtrerede tal er skrevet til filtered.txt")
            self.state = 'færdig'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = FiltreringTilstandsmaskine()
sm.transition('læs_fil')
sm.transition('filtrer_tal')
sm.transition('skriv_fil')

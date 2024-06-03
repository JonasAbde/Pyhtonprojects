class TilfoejOgBeregnSumTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.filename = 'tal.txt'
        self.numbers = []

    def transition(self, event):
        if self.state == 'start' and event == 'tilfoej_tal':
            nye_tal = input("Indtast tal adskilt af komma: ").split(',')
            self.numbers = [int(num.strip()) for num in nye_tal]
            with open(self.filename, 'a') as file:
                for number in self.numbers:
                    file.write(f"{number}\n")
            print("Tallene er blevet tilføjet til filen.")
            self.state = 'tilføjet'
        elif self.state == 'tilføjet' and event == 'beregn_sum':
            try:
                with open(self.filename, 'r') as file:
                    alle_tal = [int(line.strip()) for line in file]
                total_sum = sum(alle_tal)
                print(f"Summen af alle tal: {total_sum}")
                self.state = 'beregnet'
            except FileNotFoundError:
                print(f"Fil {self.filename} blev ikke fundet.")
                self.state = 'fejl'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = TilfoejOgBeregnSumTilstandsmaskine()
sm.transition('tilfoej_tal')
sm.transition('beregn_sum')

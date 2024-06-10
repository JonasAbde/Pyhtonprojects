import random

class TalBehandlingTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.tal_10 = []

    def transition(self, event):
        if self.state == 'start' and event == 'generer_tal':
            self.tal_10 = [random.randint(0, 10) for _ in range(10)]
            self.state = 'genereret'
            print(f"Genererede tal: {self.tal_10}")
        elif self.state == 'genereret' and event == 'tilfoej_tal':
            sum_val = sum(self.tal_10)
            self.tal_10.append(sum_val)
            print(f"Tilføjet summen af tallene: {sum_val}")
            self.state = 'tilføjet'
        elif self.state == 'tilføjet' and event == 'sorter_tal':
            self.tal_10.sort()
            print(f"Sorterede tal: {self.tal_10}")
            self.state = 'sorteret'
        elif self.state == 'sorteret' and event == 'skriv_til_fil':
            with open('list100.txt', 'w') as file:
                for number in self.tal_10:
                    file.write(f"{number}\n")
            print("Tallene er skrevet til list100.txt")
            self.state = 'færdig'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = TalBehandlingTilstandsmaskine()
sm.transition('generer_tal')
sm.transition('tilfoej_tal')
sm.transition('sorter_tal')
sm.transition('skriv_til_fil')

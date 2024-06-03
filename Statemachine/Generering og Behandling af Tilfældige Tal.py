import random

class TilfaeldigeTalTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.tal_100 = []

    def transition(self, event):
        if self.state == 'start' and event == 'generer_tal':
            self.tal_100 = [random.randint(0, 100) for _ in range(10)]
            self.state = 'genereret'
            print(f"Genererede tal: {self.tal_100}")
        elif self.state == 'genereret' and event == 'udskriv_50_100':
            print("Tal mellem 50 og 100:")
            for number in self.tal_100:
                if 50 <= number <= 100:
                    print(number)
            self.state = 'udskrevet'
        elif self.state == 'udskrevet' and event == 'tilfoej_max_min_sum':
            max_val = max(self.tal_100)
            min_val = min(self.tal_100)
            self.tal_100.append(max_val + min_val)
            print(f"Tilføjet max + min: {max_val} + {min_val} = {max_val + min_val}")
            self.state = 'tilføjet'
        elif self.state == 'tilføjet' and event == 'skriv_til_fil':
            with open('list100.txt', 'w') as file:
                for number in self.tal_100:
                    file.write(f"{number}\n")
            print("Tallene er skrevet til list100.txt")
            self.state = 'færdig'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = TilfaeldigeTalTilstandsmaskine()
sm.transition('generer_tal')
sm.transition('udskriv_50_100')
sm.transition('tilfoej_max_min_sum')
sm.transition('skriv_til_fil')

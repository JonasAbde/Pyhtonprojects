class TilfoejNavneTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.filename = 'navne.txt'

    def transition(self, event):
        if self.state == 'start' and event == 'tilfoej_navne':
            navne = input("Indtast navne adskilt af komma: ").split(',')
            with open(self.filename, 'a') as file:
                for name in navne:
                    file.write(f"{name.strip()}\n")
            print("Navnene er blevet tilføjet til filen.")
            self.state = 'tilføjet'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = TilfoejNavneTilstandsmaskine()
sm.transition('tilfoej_navne')

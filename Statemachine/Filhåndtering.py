class FilHaandteringTilstandsmaskine:
    def __init__(self):
        self.state = 'start'
        self.filename = 'list100.txt'
        self.numbers = []

    def transition(self, event):
        if self.state == 'start' and event == 'hent_fil':
            try:
                with open(self.filename, 'r') as file:
                    self.numbers = [int(line.strip()) for line in file]
                print(f"Hentede tal: {self.numbers}")
                self.state = 'hentet'
            except FileNotFoundError:
                print(f"Fil {self.filename} blev ikke fundet.")
                self.state = 'fejl'
        elif self.state == 'hentet' and event == 'tilfoej_tal':
            try:
                nye_tal = input("Indtast 3 tal mellem 0 og 100, adskilt af komma: ").split(',')
                nye_tal = [int(num) for num in nye_tal if 0 <= int(num) <= 100]
                if len(nye_tal) != 3:
                    raise ValueError("Du skal indtaste præcis 3 gyldige tal.")
                self.numbers.extend(nye_tal)
                print(f"Tilføjet tal: {nye_tal}")
                self.state = 'tilføjet'
            except ValueError as e:
                print(f"Fejl: {e}")
                self.state = 'fejl'
        elif self.state == 'tilføjet' and event == 'udskriv_tal':
            print(f"Tal i filen {self.filename}: {self.numbers}")
            self.state = 'udskrevet'
        elif self.state == 'udskrevet' and event == 'fil_status':
            print(f"Fil: {self.filename}")
            print(f"Er lukket: {True}")
            print(f"Mode: Ikke relevant efter filen er lukket")
            self.state = 'færdig'
        else:
            print(f"Ugyldig overgang fra {self.state} ved {event} hændelse.")

# Eksempel brug
sm = FilHaandteringTilstandsmaskine()
sm.transition('hent_fil')
sm.transition('tilfoej_tal')
sm.transition('udskriv_tal')
sm.transition('fil_status')
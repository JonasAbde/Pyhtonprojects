class FilTilstandsMaskine:
    def __init__(self):
        self.tilstand = 'IDLE'
        self.fil_indhold = ""

    def håndter_hændelse(self, hændelse):
        if self.tilstand == 'IDLE':
            if hændelse == 'læse_fil':
                self.læse_fil()
            elif hændelse == 'skrive_fil':
                self.skrive_fil()
            elif hændelse == 'gem_fil':
                self.gem_fil()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'LÆSER_FIL':
            if hændelse == 'fil_læst':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'SKRIVER_FIL':
            if hændelse == 'fil_skrev':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'GEMMER_FIL':
            if hændelse == 'fil_gemt':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

    def læse_fil(self):
        print("Læser fil...")
        self.fil_indhold = "Dette er filens indhold."
        self.tilstand = 'LÆSER_FIL'
        self.håndter_hændelse('fil_læst')

    def skrive_fil(self):
        print("Skriver til fil...")
        self.fil_indhold = "Nyt indhold til filen."
        self.tilstand = 'SKRIVER_FIL'
        self.håndter_hændelse('fil_skrev')

    def gem_fil(self):
        print("Gemmer fil...")
        with open('fil.txt', 'w') as f:
            f.write(self.fil_indhold)
        self.tilstand = 'GEMMER_FIL'
        self.håndter_hændelse('fil_gemt')

    def idle(self):
        print("Tilbage til IDLE...")
        self.tilstand = 'IDLE'

    def ugyldig_hændelse(self, hændelse):
        print(f"Ugyldig hændelse '{hændelse}' i tilstand '{self.tilstand}'")

# Eksempel på brug
fil_maskine = FilTilstandsMaskine()
fil_maskine.håndter_hændelse('læse_fil')
fil_maskine.håndter_hændelse('skrive_fil')
fil_maskine.håndter_hændelse('gem_fil')

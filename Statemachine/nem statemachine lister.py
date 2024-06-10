class ListeTilstandsMaskine:
    def __init__(self):
        self.tilstand = 'IDLE'
        self.liste = []

    def håndter_hændelse(self, hændelse):
        if self.tilstand == 'IDLE':
            if hændelse == 'tilføj_element':
                self.tilføj_element()
            elif hændelse == 'fjern_element':
                self.fjern_element()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'TILFØJER_ELEMENT':
            if hændelse == 'element_tilføjet':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'FJERNER_ELEMENT':
            if hændelse == 'element_fjernet':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

    def tilføj_element(self):
        print("Tilføjer element til listen...")
        self.liste.append("nyt element")
        self.tilstand = 'TILFØJER_ELEMENT'
        self.håndter_hændelse('element_tilføjet')

    def fjern_element(self):
        print("Fjerner element fra listen...")
        if self.liste:
            self.liste.pop()
        self.tilstand = 'FJERNER_ELEMENT'
        self.håndter_hændelse('element_fjernet')

    def idle(self):
        print("Tilbage til IDLE...")
        self.tilstand = 'IDLE'

    def ugyldig_hændelse(self, hændelse):
        print(f"Ugyldig hændelse '{hændelse}' i tilstand '{self.tilstand}'")


# Eksempel på brug
liste_maskine = ListeTilstandsMaskine()
liste_maskine.håndter_hændelse('tilføj_element')
liste_maskine.håndter_hændelse('fjern_element')

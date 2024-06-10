class PasswordTilstandsMaskine:
    def __init__(self):
        self.tilstand = 'IDLE'
        self.user1_password = ""
        self.user2_password = ""

    def håndter_hændelse(self, hændelse):
        if self.tilstand == 'IDLE':
            if hændelse == 'opret_password':
                self.opret_password()
            elif hændelse == 'valider_password':
                self.valider_password()
            elif hændelse == 'ændre_password':
                self.ændre_password()
            elif hændelse == 'stop':
                self.stop()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'OPRETTER_PASSWORD':
            if hændelse == 'password_oprettet':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'VALIDERER_PASSWORD':
            if hændelse == 'password_valideret':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

        elif self.tilstand == 'ÆNDRER_PASSWORD':
            if hændelse == 'password_ændret':
                self.idle()
            else:
                self.ugyldig_hændelse(hændelse)

    def opret_password(self):
        print("Opretter passwords...")
        brugertype = input("Er det bruger1 eller bruger2 password (bruger1/bruger2)? ")
        nyt_password = input("Indtast nyt password: ")
        if brugertype == 'bruger1':
            self.user1_password = nyt_password
        elif brugertype == 'bruger2':
            self.user2_password = nyt_password
        else:
            print("Ugyldig brugertype.")
            self.idle()
            return
        self.tilstand = 'OPRETTER_PASSWORD'
        self.håndter_hændelse('password_oprettet')
        self.file(f"Oprettet password for {brugertype}", "******")

    def valider_password(self):
        print("Validerer password...")
        brugertype = input("Er det bruger1 eller bruger2 password (bruger1/bruger2)? ")
        indtastet_password = input("Indtast password for at validere: ")
        if brugertype == 'bruger1' and indtastet_password == self.user1_password:
            print("Bruger1-password valideret korrekt.")
            self.tilstand = 'VALIDERER_PASSWORD'
            self.håndter_hændelse('password_valideret')
        elif brugertype == 'bruger2' and indtastet_password == self.user2_password:
            print("Bruger2-password valideret korrekt.")
            self.tilstand = 'VALIDERER_PASSWORD'
            self.håndter_hændelse('password_valideret')
        else:
            print("Forkert password.")
            self.idle()

    def ændre_password(self):
        print("Ændrer password...")
        brugertype = input("Er det bruger1 eller bruger2 password (bruger1/bruger2)? ")
        indtastet_password = input("Indtast nuværende password: ")
        if brugertype == 'bruger1' and indtastet_password == self.user1_password:
            nyt_password = input("Indtast nyt password: ")
            self.user1_password = nyt_password
            print("Bruger1-password ændret succesfuldt.")
            self.tilstand = 'ÆNDRER_PASSWORD'
            self.håndter_hændelse('password_ændret')
            self.file(f"Ændret bruger1-password", "******")
        elif brugertype == 'bruger2' and indtastet_password == self.user2_password:
            nyt_password = input("Indtast nyt password: ")
            self.user2_password = nyt_password
            print("Bruger2-password ændret succesfuldt.")
            self.tilstand = 'ÆNDRER_PASSWORD'
            self.håndter_hændelse('password_ændret')
            self.file(f"Ændret bruger2-password", "******")
        else:
            print("Forkert nuværende password.")
            self.idle()

    def idle(self):
        print("Tilbage til IDLE...")
        self.tilstand = 'IDLE'

    def stop(self):
        print("Stopper tilstandsmaskinen...")
        exit()

    def ugyldig_hændelse(self, hændelse):
        print(f"Ugyldig hændelse '{hændelse}' i tilstand '{self.tilstand}'")
        self.idle()

    def file(self, beskrivelse, password):
        with open("passwords.txt", "a") as f:
            f.write(f"{beskrivelse}: {password}\n")
            f.close()


# Eksempel på brug
password_maskine = PasswordTilstandsMaskine()


def menu():
    print(
        "1) Opret password\n"
        "2) Valider password\n"
        "3) Ændre password\n"
        "4) Stop"
    )
    valg = int(input("Indtast dit valg her: "))
    if valg == 1:
        password_maskine.håndter_hændelse('opret_password')
    elif valg == 2:
        password_maskine.håndter_hændelse('valider_password')
    elif valg == 3:
        password_maskine.håndter_hændelse('ændre_password')
    elif valg == 4:
        password_maskine.håndter_hændelse('stop')
    else:
        print("Prøv igen")
        menu()


# Start menu
menu()

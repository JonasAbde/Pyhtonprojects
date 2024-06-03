"""
Denied: Når brugeren ikke har adgang.
Granted: Når brugeren har adgang.
"""


# Definér en faktisk adgangskode
korrekt_adgangskode = "1234"

def start():
    # Bed brugeren om at indtaste adgangskoden
    indtastet_adgangskode = input("Hvad er adgangskoden? ")
    # Kontroller adgangskoden og print resultatet
    adgangs_kontrol(indtastet_adgangskode)

def adgangs_kontrol(indtastet_adgangskode):
    if indtastet_adgangskode == korrekt_adgangskode:
        print("Adgang.")
    else:
        print("Adgang nægtet.")
        # Her kan du vælge at kalde start() igen, hvis du vil tillade flere forsøg
        start()

# Start programmet
start()



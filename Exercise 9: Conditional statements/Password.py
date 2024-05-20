def tjek_adgang():
    """Beder brugeren om alder og kodeord, og giver adgang hvis betingelserne er opfyldt."""

    while True:  # Løkke for at sikre gyldig alder
        try:
            alder = int(input("Indtast din alder: "))
            if alder > 0:
                break
            else:
                print("Alder skal være et positivt tal. Prøv igen.")
        except ValueError:
            print("Ugyldig indtastning. Indtast venligst et tal.")

    kodeord = input("Indtast kodeord: ")
    korrekt_kodeord = "hemmeligt"  # Erstat med det rigtige kodeord

    if alder > 20 and kodeord == korrekt_kodeord:
        print("Adgang givet! Velkommen.")
    else:
        if alder <= 20:
            print("Din alder opfylder ikke kravene.")
        if kodeord != korrekt_kodeord:
            print("Forkert kodeord.")
        print("Adgang nægtet.")

if __name__ == "__main__":
    tjek_adgang()

def omgangstider():
    """Beregner hurtigste, langsomste og gennemsnitlige omgangstider."""

    antal_omgange = int(input("Hvor mange omgange løb du? "))

    omgangstider = []  # En liste til at gemme tiderne

    for omgang in range(1, antal_omgange + 1):
        while True:  # Loop for at sikre gyldig indtastning
            try:
                tid = float(input(f"Indtast tid for omgang {omgang} (i sekunder): "))
                if tid > 0:  # Tjek om tiden er positiv
                    omgangstider.append(tid)  # Gem tiden i listen
                    break  # Afslut while-løkken
                else:
                    print("Omgangstid skal være positiv. Prøv igen.")
            except ValueError:
                print("Ugyldig indtastning. Indtast venligst et tal.")

    hurtigste_omgang = min(omgangstider)
    langsomste_omgang = max(omgangstider)
    gennemsnitlig_omgang = sum(omgangstider) / antal_omgange

    print("\nResultater:")
    print(f"Hurtigste omgang: {hurtigste_omgang:.2f} sekunder")
    print(f"Langsomste omgang: {langsomste_omgang:.2f} sekunder")
    print(f"Gennemsnitlig omgangstid: {gennemsnitlig_omgang:.2f} sekunder")

if __name__ == "__main__":
    omgangstider()

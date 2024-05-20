def gennemsnitlig_ordlængde():
    """Beregner den gennemsnitlige længde af indtastede ord."""

    ord = []  # Liste til at gemme ordene
    samlet_længde = 0
    antal_ord = 0

    while True:
        ord_input = input("Indtast et ord (eller tryk enter for at afslutte): ")
        if not ord_input:  # Tjek om input er tomt
            break  # Afslut løkken
        ord.append(ord_input)  # Tilføj ordet til listen
        samlet_længde += len(ord_input)  # Opdater samlet længde
        antal_ord += 1  # Opdater antal ord

    if antal_ord > 0:
        gennemsnit = round(samlet_længde / antal_ord)  # Beregn gennemsnit
        print(f"\nGennemsnitlig ordlængde: {gennemsnit}")
    else:
        print("Ingen ord blev indtastet.")

if __name__ == "__main__":
    gennemsnitlig_ordlængde()

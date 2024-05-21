def calculate_automobile_costs():
    """
    Beregn og vis de samlede månedlige og årlige omkostninger ved at drive en bil baseret på brugerinput.
    """
    # Bed brugeren om at indtaste de månedlige omkostninger
    loan_payment = float(input("Indtast månedlige omkostninger for lån: "))
    insurance = float(input("Indtast månedlige omkostninger for forsikring: "))
    gas = float(input("Indtast månedlige omkostninger for benzin: "))
    oil = float(input("Indtast månedlige omkostninger for olie: "))
    tires = float(input("Indtast månedlige omkostninger for dæk: "))
    maintenance = float(input("Indtast månedlige omkostninger for vedligeholdelse: "))

    # Beregn de samlede månedlige omkostninger
    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance

    # Beregn de samlede årlige omkostninger
    total_annual_cost = total_monthly_cost * 12

    # Vis resultaterne
    print(f"\nSamlede månedlige omkostninger: {total_monthly_cost:.2f} kr.")
    print(f"Samlede årlige omkostninger: {total_annual_cost:.2f} kr.")

# Kald funktionen for at udføre programmet
calculate_automobile_costs()

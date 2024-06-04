def beregn_serie_og_parallel():
    R1 = float(input("Indtast værdi for R1: "))
    R2 = float(input("Indtast værdi for R2: "))
    V = float(input("Indtast værdi for V (spænding): "))

    R_parallel = 1 / ((1 / R1) + (1 / R2))
    print(f"Den samlede parallel modstand er: {R_parallel}")

    R3 = float(input("Indtast værdi for R3: "))
    R_total = R_parallel + R3
    print(f"Den samlede modstand i serie er: {R_total}")

    I = V / R_total
    print(f"Strømmen (I) er: {I}")

    with open("modstand.txt", "a") as fil:
        fil.write(f"V = {V}, R_parallel = {R_parallel}, R_total = {R_total}, I = {I}\n")
    print("Beregning gemt i modstand.txt")


# Hovedprogram
beregn_serie_og_parallel()

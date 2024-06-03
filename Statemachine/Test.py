def parallel_regning():
    volt = float(input("Indtast mængde volt: "))
    R1 = float(input("Indtast modstand et i ohm: "))
    R2 = float(input("Indtast modstand to i ohm: "))
    parallel_sum = 1 / (1/R1 + 1/R2)
    print(f"Samlede parallelle modstand = {parallel_sum} ohm")
    return volt, parallel_sum

def serie_regning(R_parallel):
    R3 = float(input("Indtast modstand tre i ohm: "))
    R_serie = R_parallel + R3
    print(f"Samlede serie modstand = {R_serie} ohm")
    return R_serie

def sum_modstand():
    print("For at finde samlede modstand i kredsløb skal vi lægge serie og parallel modstand sammen")
    volt, R_parallel = parallel_regning()
    R_total = serie_regning(R_parallel)
    stroem = volt / R_total
    print(f"Samlede modstand (R_total) = {R_total} ohm")
    print(f"Stroem (I) = {stroem} ampere")
    save_to_file(volt, R_total, stroem)

def save_to_file(volt, R_total, stroem, filnavn="modstand.txt"):
    data = f"Spaending (U): {volt} V, Samlede modstand (R_total): {R_total} ohm, Strøm (I): {stroem} A"
    with open(filnavn, "a") as file:
        file.write(data + "\n")
    print("Data gemt til filen modstand.txt")

if __name__ == "__main__":
    sum_modstand()

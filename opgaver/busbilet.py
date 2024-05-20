# indsatning fra brugeren for start og slut zone
start_zone = int(input("Indtast start zone: "))
slut_zone = int(input("Indtast slut zone: "))

# Antal zoner rejst
antal_zoner = abs(start_zone - slut_zone) + 1

# Pris per zone
pris_per_zone = 30

# Total pris uden rabat
total_pris = antal_zoner * pris_per_zone

# Hvis der rejser mere end 2 zoner, gives der 10% rabat
if antal_zoner > 2:
    total_pris *= 0.9

#  den totale pris for busrejsen
print("Den totale pris for busrejsen er:", total_pris, "kr.")


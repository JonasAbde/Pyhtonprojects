# I denne python kode, vil jeg vise hvordan bus billetten kan udregnes.

zone_pris = 30  # pris per zone

zone_rabat = 0.10  # Zone rabat

print("INFO: Ved at rejse mere end 2 zoner gives der 10% i rabat på din samlede betaling :)")

zone_start = float(input("Vælg din start zone"))  # vedkommendes start zone
print(f"du har valgt zone {zone_start} som din start zone")

# Her spørges der om hvor mange zoner brugeren ønsker at køre
ønsket_antal_zoner = float(input("Hvor mange zoner ønsker du at køre?"))

pris_sum = ønsket_antal_zoner * zone_pris  # Udregning af pris sum uden rabat

print("dette er din prisen uden rabat")
print(pris_sum)

if ønsket_antal_zoner > 2:
    print("dette er din pris nu med 10% rabat")
    print(pris_sum - (zone_rabat * pris_sum))  # Udregning af pris sum med rabat

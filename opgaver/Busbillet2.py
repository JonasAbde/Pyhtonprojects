# Definerign af prisen per zone
pris_per_zone = 30

# Indhent antallet af zoner fra brugeren
zoner = float(input("Indtast antal zoner, du vil rejse: "))

# Beregn den samlede pris uden rabat
total_pris = zoner * pris_per_zone

# Tjek om der skal gives rabat for kørsel over 2 zoner
if zoner > 2:  # Beregn rabatten og træk den fra den totale pris
    rabat_givet = total_pris * 0.1  # 10% rabat

total_pris = rabat_givet - total_pris

# Udskriv den endelige billetpris
print(f"Den samlede pris for din busbillet er: {total_pris} kroner")

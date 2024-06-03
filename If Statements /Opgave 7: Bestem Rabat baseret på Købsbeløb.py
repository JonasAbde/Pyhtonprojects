# Opgavebeskrivelse:
# Skriv et program, der bestemmer rabatten baseret på købsbeløbet og udskriver rabatten.

def beregn_rabat(beløb):
    if beløb < 100:
        rabat = 0.05
    elif 100 <= beløb <= 500:
        rabat = 0.10
    else:
        rabat = 0.15
    rabat_beløb = beløb * rabat
    print(f"Rabat: {rabat * 100}%, Rabat beløb: {rabat_beløb} kr")

# Eksempel brug
beregn_rabat(50)
beregn_rabat(200)
beregn_rabat(600)

# Hvad der sker:
# - Vi bruger en if-elif-else struktur til at bestemme rabatsatsen baseret på 'beløb'.
# - Vi beregner rabat_beløbet ved at multiplicere 'beløb' med rabatsatsen.
# - Vi udskriver rabatsatsen og rabat_beløbet.

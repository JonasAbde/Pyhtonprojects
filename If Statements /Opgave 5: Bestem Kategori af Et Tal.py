# Opgavebeskrivelse:
# Skriv et program, der bestemmer hvilken kategori et givet tal falder ind under og udskriver en passende besked.

def tjek_kategori(tal):
    if tal < 0:
        print("Negativt tal.")
    elif 0 <= tal <= 10:
        print("Enkelt tal.")
    elif 10 < tal <= 100:
        print("Dobbelt tal.")
    else:
        print("Stort tal.")

# Eksempel brug
tjek_kategori(-5)
tjek_kategori(5)
tjek_kategori(50)
tjek_kategori(150)

# Hvad der sker:
# - Vi bruger en if-elif-else struktur til at tjekke 'tal'.
# - Hvis 'tal' er mindre end 0, udskrives en besked om, at det er et negativt tal.
# - Hvis 'tal' er mellem 0 og 10 (inklusive), udskrives en besked om, at det er et enkelt tal.
# - Hvis 'tal' er mellem 10 og 100 (ikke inklusive 10, men inklusive 100), udskrives en besked om, at det er et dobbelt tal.
# - Hvis 'tal' er større end 100, udskrives en besked om, at det er et stort tal.

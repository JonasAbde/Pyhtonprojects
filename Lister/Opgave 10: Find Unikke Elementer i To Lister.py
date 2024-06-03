def unikke_elementer(liste1, liste2):
    # Brug set() og ^ operatoren til at finde unikke elementer
    return list(set(liste1) ^ set(liste2))

# Eksempel brug
liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]
print(f"Unikke elementer: {unikke_elementer(liste1, liste2)}")

# Hvad der sker:
# - set(liste1) skaber et sæt af elementerne i 'liste1'.
# - set(liste2) skaber et sæt af elementerne i 'liste2'.
# - set(liste1) ^ set(liste2) returnerer et sæt af de unikke elementer mellem de to sæt.
# - Vi konverterer det unikke sæt tilbage til en liste ved hjælp af list().
# - Vi returnerer listen af unikke elementer.
# - Vi udskriver listen af unikke elementer ved at kalde unikke_elementer() funktionen med 'liste1' og 'liste2' som argumenter.
# - Funktionen returnerer listen af unikke elementer, som vi udskriver.
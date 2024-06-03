def fælles_elementer(liste1, liste2):
    # Brug set() og & operatoren til at finde fælles elementer
    return list(set(liste1) & set(liste2))

# Eksempel brug
liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]
print(f"Fælles elementer: {fælles_elementer(liste1, liste2)}")

# Hvad der sker:
# - set(liste1) skaber et sæt af elementerne i 'liste1'.
# - set(liste2) skaber et sæt af elementerne i 'liste2'.
# - set(liste1) & set(liste2) returnerer et sæt af de fælles elementer mellem de to sæt.
# - Vi konverterer det fælles sæt tilbage til en liste ved hjælp af list().
# - Vi returnerer listen af fælles elementer.
# - Vi udskriver listen af fælles elementer ved at kalde fælles_elementer() funktionen med 'liste1' og 'liste2' som argumenter.
# - Funktionen returnerer listen af fælles elementer, som vi udskriver.
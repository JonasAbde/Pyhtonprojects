"""
Child: Alder under 13 år.
Teenager: Alder mellem 13 og 19 år.
Adult: Alder over 19 år.
"""


def alders_gruppe(alder):
    if alder < 13:
        print("du er et barn")
    elif 13 <= alder <= 19:
        print("du er teenager")
    else:
        print("du er voksen")

# Hent alder fra brugeren
alder = int(input("Indtast alder: "))
alders_gruppe(alder)

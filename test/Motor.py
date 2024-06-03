import motor
from time import sleep

# Definer funktion til at stoppe motoren
def stop_motor():
    motor.def_motor("stop")

# Definer funktion til at starte motoren
def start_motor(direction):
    motor.def_motor(direction)

while True:
    # Brugeren vælger etage via terminal input (mocked her for eksempel)
    ønskede_etage = int(input("Indtast ønskede etage (1, 2, 3): "))

    if ønskede_etage == 1:
        print("Starter motoren mod etage 1")
        start_motor("down")  # Antag at "down" er kommandoen for at bevæge sig mod etage 1
        sleep(2)  # Simulerer tidsforbrug for at nå etage 1
        stop_motor()
        print("Motoren er stoppet ved etage 1")
    elif ønskede_etage == 2:
        print("Starter motoren mod etage 2")
        start_motor("up")  # Antag at "up" er kommandoen for at bevæge sig mod etage 2
        sleep(2)  # Simulerer tidsforbrug for at nå etage 2
        stop_motor()
        print("Motoren er stoppet ved etage 2")
    elif ønskede_etage == 3:
        print("Starter motoren mod etage 3")
        start_motor("up")  # Antag at "up" er kommandoen for at bevæge sig mod etage 3
        sleep(3)  # Simulerer tidsforbrug for at nå etage 3
        stop_motor()
        print("Motoren er stoppet ved etage 3")
    else:
        print("Ugyldigt input, prøv igen.")

    sleep(1)  # Tilføj en lille forsinkelse før næste input

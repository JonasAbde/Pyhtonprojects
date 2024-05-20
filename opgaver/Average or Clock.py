#Du må selv vælge mellem de 2 opgaver
#Gennemsnitskarakterberegner - Skal beregne gennemsnittet af et specificeret antal karakterer. Spørg brugeren om, hvor mange karakterer der skal beregnes et gennemsnit for. Opret en løkke, der beder brugeren om karaktererne, én ad gangen, indtil det angivne antal karakterer er nået. Akkumuler summen af karaktererne. Beregn og behandl det gennemsnitlige karaktergennemsnit. Udskriv det gennemsnitlige karaktergennemsnit.
#Animeret Analogt Ur Opret et animeret grafisk analogt ur ved hjælp af turtle-biblioteket. Uret skal mindst have en sekund- og en minutviser. For hvert sekund skal den lange viser rotere én sekund-tick. For hvert minut skal den korte viser rotere én minut-tick.

import turtle
import time

# Opretter skærmen
skærm = turtle.Screen()
skærm.title("Animeret Turtle Ur")
skærm.bgcolor("white")
skærm.tracer(0)  # Deaktiver automatisk opdatering

# Opret en turtle til at tegne uret
ur_turtle = turtle.Turtle()
ur_turtle.hideturtle()
ur_turtle.speed(0)  # Sæt hastigheden til den hurtigste
ur_turtle.penup()

# Funktion til at tegne urfjæset
def tegn_urfjæs(radius):
    ur_turtle.goto(0, -radius)
    ur_turtle.pendown()
    ur_turtle.circle(radius)
    ur_turtle.penup()

# Funktioner for visere
def tegn_visere():
    nu = time.localtime()  # Få lokal tid
    sekunder = nu.tm_sec
    minutter = nu.tm_min + sekunder / 60
    tegn_viser(sekunder * 6, 100, "red")  # Sekundviser roterer 360 grader / 60 sekunder
    tegn_viser(minutter * 6, 80, "blue")  # Minutviser roterer 360 grader / 60 minutter

def tegn_viser(vinkel, længde, farve):
    ur_turtle.goto(0, 0)
    ur_turtle.setheading(90 - vinkel)  # Juster rotationen
    ur_turtle.pendown()
    ur_turtle.color(farve)
    ur_turtle.forward(længde)
    ur_turtle.penup()

# Funktion til at opdatere uret
def opdater_ur():
    ur_turtle.clear()  # Ryd tegningen for at tegne viserne igen
    tegn_urfjæs(100)
    tegn_visere()
    skærm.update()  # Opdater skærmen for at vise ændringerne
    skærm.ontimer(opdater_ur, 1000)  # Sæt timer til at opdatere uret hvert sekund

tegn_urfjæs(150)
opdater_ur()

# Hold vinduet åbent, indtil det lukkes manuelt
skærm.mainloop()
#https://www.w3schools.com/python/python_datetime.asp
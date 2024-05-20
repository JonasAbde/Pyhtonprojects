import turtle

def tegn_stopskilt():
    """Tegner et ottekantet stopskilt med centreret tekst."""

    # Opsæt skærmen og pennen
    skærm = turtle.Screen()
    skærm.setup(width=500, height=500)  # Vindusstørrelse
    pen = turtle.Turtle()
    pen.speed(0)  # Hurtigste tegnehastighed

    # Tegn ottekanten (stopskiltformen)
    sidelængde = 100
    pen.penup()  # Løft pennen for at undgå at tegne mens den flyttes
    pen.goto(-sidelængde / 2, sidelængde / 2)  # Startposition (øverst til venstre)
    pen.pendown()  # Sæt pennen ned for at begynde at tegne
    pen.fillcolor("red")  # Fyldfarve rød
    pen.begin_fill()
    for _ in range(8):  # Tegn de otte sider
        pen.forward(sidelængde)
        pen.right(45)  # Drej 45 grader til højre
    pen.end_fill()  # Afslut fyldningen

    # Skriv "STOP" i midten
    pen.penup()
    pen.goto(0, -sidelængde / 4)  # Flyt til midten
    pen.color("white")  # Skriftfarve hvid
    pen.write("STOP", align="center", font=("Arial", 30, "bold"))  # Skriv STOP med fed skrift

    # Skjul pennen og hold vinduet åbent
    pen.hideturtle()
    skærm.exitonclick()  # Vent på klik for at lukke vinduet

if __name__ == "__main__":
    tegn_stopskilt()

# Øvelse 4 - Personal Web Page Generator
# Skriv et program, der beder brugeren om hans eller hendes navn og en sætning, der beskriver sig selv.
# Programmet skal derefter oprette en HTML-fil, der indeholder input til en simpel webside.

if __name__ == "__main__":
    # Brugeren indtaster sit navn
    navn = input("Indtast dit navn: ")

    # Brugeren indtaster en sætning, der beskriver sig selv
    beskrivelse = input("Indtast en sætning, der beskriver dig selv: ")

    # HTML-indholdet til websiden
    html_content = f"""<html>
<head>
</head>
<body>
<center>
<h1>{navn}</h1>
</center>
<hr />
{beskrivelse}
<hr />
</body>
</html>"""

    # Opretter og skriver til HTML-filen
    with open("personal_web_page.html", "w") as file:
        file.write(html_content)

    print("HTML-filen 'personal_web_page.html' er blevet oprettet med dit indhold.")

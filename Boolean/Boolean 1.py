"""Skriv en betingelse, der tjekker om en variabel a er større
end 10 og en variabel b er mindre end 20."""


#eksempel 1
a = 10
b = 20

if a > b:
    print(f"{a} er ikke større end {b}")
if a < b:
    print(f"{a} er mindre end {b}")


# Eksempel 2

a = 10
b = 20

if a > 10 and b < 20:
    print(f"{a} er større end 10 og {b} er mindre end 20")
else:
    print(f"{a} er ikke større end 10, eller {b} er ikke mindre end 20")

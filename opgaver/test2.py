x = float(input("Indtast en x-værdi"))
y = float(input("Indtast en y-værdi"))

operator = input("du kan vælge mellem plus/dividere/gange/minus")

if operator == "plus":
    print(f"x+y={x + y}")
    print()
if operator == "dividere":
    print(f"x/y={x / y})")
    print()
if operator == "gange":
    print(f"x*y={x * y})")
    print()
if operator == "minus":
    print(f"x-y={x - y})")
    print()

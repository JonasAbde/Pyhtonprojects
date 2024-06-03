# her er en loop som spørger brugeren om et tal, produktet af det tal skal lægges sammen med 10
# med mindre produktet er større end 100

product = 0  # Initialize the product to be 0

while product < 100:

    number = float(input("indtast tal: "))  # tal fra brugeren
    product = number * 10  # gange med 10
    print(f"The product is {product}")  # en print af produktet gange 10

print("The product is now 100 or greater.")

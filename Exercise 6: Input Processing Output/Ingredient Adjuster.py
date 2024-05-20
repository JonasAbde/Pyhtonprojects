#Ingredient adjuster
#A cookie recipe calls for the following ingredients:
#1.5 cups of sugar
#1 cup of butter
#2.75 cups of flour
#The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user how
#many cookies he or she wants to make, the display the number of cups of each ingredient needed for the
#specified number of cookies.


# mængder for 48 cookies = 1.5 cups sukker, 1 cup smør, 2.75 cups mel
ingredienser = {
    'sukker': 1.5,  # cups
    'smør': 1,      # cups
    'mel': 2.75     # cups
}

# Antal cookies opskriften er beregnet til (maks 48 stk)
cookies_original = 48

# hvor mange cookies man ønsker at lave
onsket_cookies = int(input("Hvor mange cookies ønsker du at lave? "))

# Beregner forholdet for  af ingrediensmængder
forhold = onsket_cookies / cookies_original

# printer i terminal den justerede mængde af hver ingrediens
print(f"For at lave {onsket_cookies} cookies, skal du bruge:")

for ingrediens, mængde in ingredienser.items():
    justeret_mængde = mængde * forhold
    print(f"{justeret_mængde:.8f} cups af {ingrediens}")



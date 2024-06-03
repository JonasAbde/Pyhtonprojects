# Write a while loop that asks the user to enter two numbers. The numbers should be added and the
# sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If
# so, the loop should repeat, otherwise it should terminate.

while True:
    tal1 = float(input("indtast dit ene tal"))
    tal2 = float(input("indtast dit andet tal"))

    sum_of_numbers = tal1 + tal2
    print(f"The sum is: {sum_of_numbers}")

    # Ask the user if they want to perform the operation again
    repeat = input("ønsker du at gentage denne operation (ja/nej): ")

    # hvis bruger ikke ønsker at forsætte, break loop
    if repeat != "ja":
        break

# færdiggørelse af loop
print("Operation færdig.")

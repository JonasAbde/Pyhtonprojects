# Write a loop that uses the range function to display all odd numbers between 1 and 100

square = 0
number = 1

while square < 99:
    square = number ** 2
    if square >= 99:
        break
    print(square)
    number += 1

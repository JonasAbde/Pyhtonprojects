# Exercise 1 – Algorithm Workbench

# 1. Write a while loop that lets the user enter a number. The number should be multiplied by 10,
# and the result assigned to a variable named `product`. The loop should iterate as long as `product` is less than 100.

def exercise_1_1():
    while True:
        number = float(input("Enter a number: "))
        product = number * 10
        print(f"Product: {product}")
        if product >= 100:
            break

# 2. Write a while loop that asks the user to enter two numbers. The numbers should be added and the
# sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If
# so, the loop should repeat, otherwise it should terminate.

def exercise_1_2():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        sum = num1 + num2
        print(f"Sum: {sum}")
        again = input("Do you wish to perform the operation again? (yes/no): ")
        if again.lower() != "yes":
            break

# 3. Write a loop that uses the range function to display all odd numbers between 1 and 100.

def exercise_1_3():
    for i in range(1, 101, 2):
        print(i)

# 4. Starting with a variable `text` containing an empty string, write a loop that prompts the user to type
# a word. Add the user's input to the end of `text` and then print the variable. The loop should repeat
# while the length of `text` is less than 10 characters.

def exercise_1_4():
    text = ""
    while len(text) < 10:
        word = input("Type a word: ")
        text += word
        print(f"Text: {text}")

# 5. Write a loop that calculates the total of the following series of numbers: `1/30 + 2/29 + 3/28 + ... + 30/1`

def exercise_1_5():
    total = 0
    for i in range(1, 31):
        total += i / (31 - i)
    print(f"Total: {total}")

# Main function to run all exercises
def main():
    print("Exercise 1.1")
    exercise_1_1()
    print("\nExercise 1.2")
    exercise_1_2()
    print("\nExercise 1.3")
    exercise_1_3()
    print("\nExercise 1.4")
    exercise_1_4()
    print("\nExercise 1.5")
    exercise_1_5()

if __name__ == "__main__":
    main()

def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    # Ask for height and weight
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    # Print the calculated BMI value
    print(f"Your BMI is: {bmi:.2f}")

    # Find and print the meaning
    meaning = interpret_bmi(bmi)
    print(f"This means you are: {meaning}")


if __name__ == "__main__":
    main()

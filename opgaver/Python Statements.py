# Define example values for x and a
x = 150  # Example value greater than 100
a = 50   # Example value less than 100

# 1. Write an “if statement” that assigns 20 to the variable y, and assigns 40 to the variable z if the variable x is greater than 100.
if x > 100:
    y = 20
    z = 40
else:
    y = None
    z = None

# Print the result for the first task
print(f"Task 1: y = {y}, z = {z}")

# 2. Write an “if statement” that assigns 10 to the variable b and 50 to the variable c if the variable a is equal to 100.
if a == 100:
    b = 10
    c = 50
else:
    b = None
    c = None

# Print the result for the second task
print(f"Task 2: b = {b}, c = {c}")

# 3. Write an “if-else statement” that assigns 0 to the variable b if the variable a is less than 10. Otherwise, it should assign 99 to the variable b.
if a < 10:
    b = 0
else:
    b = 99

# Print the result for the third task
print(f"Task 3: b = {b}")

# 4. Explain what is meant by the term “conditionally executed”.
# Conditionally executed refers to code that runs only if a specific condition or set of conditions is true.
# In programming, this often involves using if, elif, and else statements to control the flow of execution based on boolean expressions.
# If the condition evaluates to True, the code block within the if statement is executed.
# If it evaluates to False, the program may execute a different block of code (in the case of else) or skip the block entirely.

# 5. Explain how a single alternative decision structure and a dual alternative decision structure differ.
# A single alternative decision structure involves only one condition and provides a single path of execution if the condition is true.
# If the condition is false, the program simply continues to the next statement after the decision structure. This is typically represented by an if statement without an accompanying else.
# Example of a single alternative decision structure:
# if condition:
#     # Code to execute if condition is true

# A dual alternative decision structure provides two paths of execution: one if the condition is true and another if the condition is false.
# This is represented by an if statement followed by an else statement.
# Example of a dual alternative decision structure:
# if condition:
#     # Code to execute if condition is true
# else:
#     # Code to execute if condition is false

#Write code that does the following: Opens number_list.txt, that was created by the code
# from problem 3, reads all the numbers from the file and displays them, then closes the file

# Open the file number_list.txt in read mode
with open('number_list.txt', 'r') as file:
    # Read all lines from the file
    numbers = file.readlines()

# Process and display each number from the list
for number in numbers:
    # Strip any trailing newlines or spaces and display the number
    print(number.strip())

# The file is automatically closed when exiting the 'with' block

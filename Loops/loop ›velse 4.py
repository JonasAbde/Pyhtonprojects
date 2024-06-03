# Starting with a variable text containing an empty string, write a loop that prompts the user to type
# a word. Add the users input to the end of text and the print the variable. The loop should repeat
# while the length of text is less than 10 characters.

text = ""
while len(text) < 10:
    # brugeren skal skrive et bogstav eller ord
    word = input("skriv et ord: ")
    # tilføj bruger input
    text += word
    # Print teksten
    print(text)

# loop slutter hvis teksten er mere end 10+ karakterer lang.
print("teksten er desværre mere end ti karakterer lang.")

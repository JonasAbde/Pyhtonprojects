tekst = "programmering"
bogstav = 'r'
antal = 0

for char in tekst:
    if char == bogstav:
        antal += 1

print(f"Bogstavet '{bogstav}' optræder {antal} gange i teksten.")

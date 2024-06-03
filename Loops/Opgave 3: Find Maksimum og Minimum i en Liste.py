tal = [5, 2, 9, 1, 7, 3]
maks = tal[0]
min = tal[0]

for nummer in tal:
    if nummer > maks:
        maks = nummer
    if nummer < min:
        min = nummer

print(f"Det største tal er: {maks}")
print(f"Det mindste tal er: {min}")

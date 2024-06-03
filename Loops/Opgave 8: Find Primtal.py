def er_primtal(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Primtal mellem 1 og 50:")
for i in range(1, 51):
    if er_primtal(i):
        print(i)

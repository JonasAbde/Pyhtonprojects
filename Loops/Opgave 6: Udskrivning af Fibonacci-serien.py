fib = [0, 1]
for i in range(2, 10):
    næste_tal = fib[i-1] + fib[i-2]
    fib.append(næste_tal)

print("De første 10 tal i Fibonacci-serien er:")
for nummer in fib:
    print(nummer)

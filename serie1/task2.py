import math

if __name__ == "__main__":
    n = int(input("Bis zu welcher Zahl willst du Primzahlen bestimmen?"))

    numbers = []

    for i in range(1, n+1):
        numbers.append(i)

    numbers[0] = None

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        for k in range(i, math.floor((n/i)) + 1):
            numbers[(i*k)-1] = None

    print(numbers)

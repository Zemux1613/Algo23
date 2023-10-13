# https://de.wikipedia.org/wiki/Heron-Verfahren
if __name__ == '__main__':
    n = int(input("Welche Wurzel soll gezogen werden?"))
    a = int(input("Welche Zahl soll radiziert werden?"))
    lastNumber = 1
    while True:
        xi = ((n - 1) * lastNumber ** n + a) / (n * lastNumber ** (n - 1))

        print(xi)

        if xi == lastNumber:
            break
        else:
            lastNumber = xi

    print(lastNumber)

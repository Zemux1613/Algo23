import math


def function(x, choose):
    if choose:
        return math.pow(x, x)
    else:
        return math.exp(x)


def deltaX(_a, _b, _n):
    return (_b - _a) / _n


def rectangleMethod(_a, _b, _n):
    dX = deltaX(_a, _b, _n)

    lowerSum = 0
    upperSum = 0
    middleSum = 0

    for i in range(_a, _b - dX + 1, dX):
        lowerSum += function(i, True)
        upperSum += function(i + dX, True)

    lowerSum *= dX
    upperSum *= dX
    middleSum = (lowerSum + upperSum) / 2

    print(f"Rectangel = {middleSum}")

def trapezoidMethod(_a, _b, _n):
    dX = (_b - _a) / _n

    middleSum = 0
    sum = 0
    for i in range(_a + dX, _b - dX + dX, dX):
        sum += function(i, True)  # You need to define the function you are integrating

    middleSum = dX * (sum + function(_a, True) / 2 + function(_b, True) / 2)

    print("Trapezoid =", middleSum)

def simpsonMethod(_a, _b, _n):
    if _n % 2 != 0:
        print("Wrong n!!!")
    else:
        dX = (_b - _a) / _n

        innerSum = 0
        index = 0

        for i in range(_a, _b + dX, dX):
            if index == 0 or index == _n:
                innerSum += function(i, True)  # You need to define the function you are integrating
            else:
                innerSum += (4 if index % 2 == 1 else 2) * function(i,True)  # You need to define the function you are integrating

            index += 1

        print("Simpson =", (dX / 3) * innerSum)

# Example usage:
_a = 0
_b = 1
_n = 10

rectangleMethod(_a, _b, _n)
trapezoidMethod(_a, _b, _n)
simpsonMethod(_a, _b, _n)

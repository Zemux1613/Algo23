import math


def pi():
    sn = 2
    n = 2
    for n in range(2, 4096):
        s2n = math.sqrt((sn ** 2) / (2 + 2 * math.sqrt(1 - (sn ** 2 / 4))))
        n = 2 * n
        PI = n * s2n

        print(f"{PI} = PI, wenn n {n} ist.")

        sn = s2n

pi()
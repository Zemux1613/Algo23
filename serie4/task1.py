dic = {1905: 7.7, 1915: 8.0, 1925: 7.9, 1935: 8.1, 1945: 8.3, 1955: 8.1, 1965: 7.9, 1975: 8.3, 1985: 8.5, 1995: 9.0, 2005: 9.2}

n = len(dic.keys())

_x = 0
xy = 0
x_square = 0

for item in dic.keys():
    _x += item
    xy += item*dic[item]
    x_square += item*item

_y = 0
for item in dic.values():
    _y += item

_x *= 1/n
_y *= 1/n

b = (xy - n*_x*_y)/(x_square - n*(_x*_x))
a = _y - b*_x

print(f"y = {a} + {b}x")
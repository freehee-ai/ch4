temp = ('bird','cat', 'dog')
b,c,d = temp
print(b,c,d)

fruits = ('사과', '배', '포도', '귤', '딸기')
a, *rest = fruits
x, y, *others = fruits
print(a, rest)
print(x,y,others)

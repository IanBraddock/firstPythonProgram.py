a = 42
b = 52
c = 62
d = 20

if c > b - a:
    print ("okay")
elif c > b:
    print ("okay")
elif c == a + d:
    print ("okay")


c = 5
while c != 0:
    print(c)
    c -= 1

c = 0
while c <= 5:
    print(c)
    c += 1    

print ("the {} is dying in the hands of the {}.").format('monster', 'enemy')

#Wir setzen eine Variable None gleich, damit das erste Element in der Liste den kleinsten Wert

x = None
print("Bevor")

for i in [9,41,12,3,74,15]:
    if x is None:
        x = i
    elif i < x:
        x = i
    print(x, i)

print("Nacher", x)
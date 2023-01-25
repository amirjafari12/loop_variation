#Man setzt zwei Varianlen gleich 0: variable1 addiert man nach jedes durchgelaufene loop mit 1:
# Variable2 addiert man mit den Zahlen in der Liste: Am ende dividiert man die zwei variablen

x = 0
y = 0
print("Bevor", x, y)

for i in [9,41,12,3,74,15]:
    x = x + 1
    y = y + i
    print(x, y, i)
print("Nacher", x, y, x/y)
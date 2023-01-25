#Um zu zählen, wie viele male ein loop durchgelaufen ist, setzen wir eine Variable gleich 0 und addieren immer eine 1, für jedes durchgelaufene loop

x = 0
print("Bevor", x)

for i in [9,41,12,3,74,15]:
    x = x + 1
    print(x,i)

print("Nacher", x)
